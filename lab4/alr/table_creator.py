from typing import Set, List, Union, Optional, Tuple, Any

from alr.grammar_visitor import GrammarVisitor
from alr.instances import Terminal, Nterminal, Rule, EPS, Table, TransitionType, END_TERMINAL_NAME


def generateFIRST(rules: [Rule]) -> dict[Nterminal, Set[Terminal]]:
    FIRST = {rule.left: set() for rule in rules}
    changed = True
    while changed:
        changed = False
        for rule in rules:
            left, right = rule.left, rule.right
            cur = getFirst(right, FIRST)
            if not cur.issubset(FIRST[left]):
                changed = True
                FIRST[left] |= cur
    return FIRST


def getFirst(cur: [Union[Terminal, Nterminal]], FIRST: dict[Nterminal, Set[Terminal]]) -> Set[Terminal]:
    if not cur:
        return {EPS}
    head = cur[0]
    if isinstance(head, Terminal):
        return {head}
    else:
        return FIRST[head] - {EPS} | (getFirst(cur[1:], FIRST) if EPS in FIRST[head] else set())


class StateException(Exception):
    pass


State = None


class State:
    def __init__(self,
                 lookaheadByHandle: Optional[dict[(int, int), Set[Terminal]]] = None,
                 rules: Optional[List[Rule]] = None,
                 FIRST: Optional[dict[Nterminal, Set[Terminal]]] = None,
                 baseState: Optional[State] = None):

        if lookaheadByHandle is not None:
            self.lookaheadByHandle = lookaheadByHandle
            return

        if rules is None or FIRST is None or baseState is None:
            raise StateException("Can not initialize state")

        self.lookaheadByHandle: dict[(int, int), Set[Terminal]] = {}
        self._generate(rules, FIRST, baseState)

    def _generate(self, rules: [Rule], FIRST: dict[Nterminal, Set[Terminal]], baseState: State):
        graph: dict[(int, int), [(int, int)]] = {}

        for handle, lookahead in baseState.lookaheadByHandle.items():
            self._fillGraph(graph, rules, FIRST, handle, lookahead)

        used: Set[Tuple[int, int]] = set()
        s: [(int, int)] = []
        for v in graph:
            if v not in used:
                self._dfs(graph, v, used, s)

        s = reversed(s)

        reverseGraph = self._generateReverseGraph(graph)

        components = {v: -1 for v in graph}
        c = 0
        for v in s:
            if components[v] == -1:
                self._scc(components, reverseGraph, v, c)
                c += 1

        lookaheadByComponent, handlesByComponent = self._initByComponents(components, c)
        condensation = self._buildCondensation(graph, components, c)

        cnt = [0 for _ in range(c)]
        for vs in condensation:
            for v in vs:
                cnt[v] += 1

        q = [i for i, cnt in enumerate(cnt) if cnt == 0]

        while q:
            cur = q.pop()
            curLookahead = lookaheadByComponent[cur]
            for handle in handlesByComponent[cur]:
                self.lookaheadByHandle[handle] = curLookahead
            for u in condensation[cur]:
                cnt[u] -= 1
                lookaheadByComponent[u] |= curLookahead
                if cnt[u] == 0:
                    q.append(u)

    def _fillGraph(self, graph, rules, FIRST, handle: (int, int), lookahead: Set[Terminal]):
        if handle in self.lookaheadByHandle:
            self.lookaheadByHandle[handle] |= lookahead
            return

        graph[handle] = []
        self.lookaheadByHandle[handle] = lookahead

        ruleNum, pos = handle
        rule = rules[ruleNum]
        if pos == len(rule.right):
            return
        cur = rule.right[pos]
        if isinstance(cur, Terminal):
            return
        nextLookahead = getFirst(rule.right[pos + 1:], FIRST)
        if EPS in nextLookahead:
            wasEps = True
            nextLookahead.remove(EPS)
        else:
            wasEps = False
        for nextRule in cur.rules:
            nextHandle = (nextRule.num, 0)
            if wasEps:
                graph[handle].append(nextHandle)
            self._fillGraph(graph, rules, FIRST, nextHandle, nextLookahead)

    def _generateReverseGraph(self, graph) -> dict[(int, int), [(int, int)]]:
        reverseGraph = {v: [] for v in graph}
        for cur, nexts in graph.items():
            for next in nexts:
                reverseGraph[next].append(cur)
        return reverseGraph

    def _dfs(self, graph, v: (int, int), used: Set[Tuple[int, int]], s: [(int, int)]):
        used.add(v)
        for u in graph[v]:
            if u not in used:
                self._dfs(graph, u, used, s)
        s.append(v)

    def _scc(self, components, reverseGraph, v: (int, int), c: int):
        components[v] = c
        for u in reverseGraph[v]:
            if components[u] == -1:
                self._scc(components, reverseGraph, u, c)

    def _initByComponents(self, components, componentsCount):
        lookaheadByComponent = [set() for _ in range(componentsCount)]
        handlesByComponent = [[] for _ in range(componentsCount)]
        for v, c in components.items():
            lookaheadByComponent[c] |= self.lookaheadByHandle[v]
            handlesByComponent[c].append(v)
        return lookaheadByComponent, handlesByComponent

    def _buildCondensation(self, graph, components, componentsCount):
        condensation = [set() for _ in range(componentsCount)]
        for v, us in graph.items():
            for u in us:
                condensation[components[v]].add(components[u])
        return condensation

    def getLookahead(self, handle: (int, int)) -> Optional[Set[Terminal]]:
        return self.lookaheadByHandle.get(handle)


def transpose(table):
    rowsCnt, columnsCnt = len(table), len(table[0])
    res = [[0] * rowsCnt for _ in range(columnsCnt)]
    for i, row in enumerate(table):
        for j, value in enumerate(row):
            res[j][i] = value
    return res


class TableGenerator:
    def __init__(self, visitor: GrammarVisitor):
        self.rules = visitor.rules
        FIRST = generateFIRST(self.rules)
        self.stateGenerator = lambda baseState: State(rules=self.rules, FIRST=FIRST, baseState=baseState)

        self.nterminals = visitor.nterminals
        self.terminals = [*visitor.terminals, Terminal(END_TERMINAL_NAME, len(visitor.terminals))]

        self.tableNterminals: [[Union[int, TransitionType]]] = [[] for _ in self.nterminals]
        self.tableTerminals: [[(TransitionType, Union[str, int])]] = [[] for _ in self.terminals]

        self.states: [State] = []
        self.curState: Optional[State] = None
        self.curIndex: Optional[int] = None
        self.toUpdate = None

    def generate(self) -> Table:
        baseHandle = (0, 0)
        baseState = State(lookaheadByHandle={baseHandle: {self.terminals[-1]}})

        curState = self.stateGenerator(baseState)
        self.states.append(curState)

        self.toUpdate = [(curState, 0)]

        updateIndex = 0
        while updateIndex < len(self.toUpdate):
            self.curState, self.curIndex = self.toUpdate[updateIndex]
            self._processCurState()
            self.toUpdate[updateIndex] = None
            updateIndex += 1

        resTableNterminals, resTableTerminals = transpose(self.tableNterminals), transpose(self.tableTerminals)
        return Table(resTableNterminals, resTableTerminals)

    def _processCurState(self):
        reducableHandles, nonReducableHandles = self._splitHandles()

        handlesByNterminalNum, handlesByTerminalNum = self._splitHandlesByType(nonReducableHandles)

        updateByNterminal = self._changeStateBy(
            handlesByNterminalNum,
            kinds=self.nterminals,
            table=self.tableNterminals,
            caseBad=lambda _: TransitionType.BAD,
            caseOk=lambda nextStateIndex: nextStateIndex
        )
        self.toUpdate += updateByNterminal

        updateByTerminal = self._changeStateBy(
            handlesByTerminalNum,
            kinds=self.terminals,
            table=self.tableTerminals,
            caseBad=lambda name: (TransitionType.BAD, f"no transition from state {self.curIndex} by terminal {name}"),
            caseOk=lambda nextStateIndex: (TransitionType.SHIFT, nextStateIndex)
        )
        self.toUpdate += updateByTerminal

        self._processReducableHandles(reducableHandles)

    def _splitHandles(self) -> ([(int, int)], [(int, int)]):
        reducableHandles, nonReducableHandles = [], []
        for handle in self.curState.lookaheadByHandle:
            ruleNum, pos = handle
            if pos == len(self.rules[ruleNum].right):
                reducableHandles.append(handle)
            else:
                nonReducableHandles.append(handle)
        return reducableHandles, nonReducableHandles

    def _splitHandlesByType(self, handles: [(int, int)]) -> (
    dict[int, Set[Tuple[int, int]]], dict[int, Set[Tuple[int, int]]]):
        handlesByNterminalNum, handlesByTerminalNum = {}, {}
        for handle in handles:
            ruleNum, pos = handle
            rule = self.rules[ruleNum]
            cur = rule.right[pos]
            handleByNum = handlesByNterminalNum if isinstance(cur, Nterminal) else handlesByTerminalNum
            if cur.num not in handleByNum:
                handleByNum[cur.num] = set()
            handleByNum[cur.num].add(handle)
        return handlesByNterminalNum, handlesByTerminalNum

    def _changeStateBy(self, handlesByNum: dict[int, Set[Tuple[int, int]]], kinds, table, caseBad, caseOk) -> [
        (State, int)]:
        updateBy = []

        for kind in kinds:
            column = table[kind.num]
            if kind.num not in handlesByNum:
                self._append(column, caseBad(kind.name))
                continue

            handles = handlesByNum[kind.num]
            nextState = self._getNextState(handles)

            if self._wasState(nextState, column, updateBy, caseOk):
                continue

            stateIndex = len(self.states)
            self.states.append(nextState)
            self._append(column, caseOk(stateIndex))
            updateBy.append((nextState, stateIndex))

        return updateBy

    def _wasState(self, nextState, curColumn, updateBy, caseOk):
        for stateIndex, state in enumerate(self.states):
            if state.lookaheadByHandle.keys() != nextState.lookaheadByHandle.keys():
                continue
            self._append(curColumn, caseOk(stateIndex))
            if state.lookaheadByHandle != nextState.lookaheadByHandle:
                curAndNextLookaheads = ((state.lookaheadByHandle[handle], nextState.lookaheadByHandle[handle])
                                        for handle in state.lookaheadByHandle.keys())
                needUpdate = False
                for cur, next in curAndNextLookaheads:
                    if not next.issubset(cur):
                        needUpdate = True
                        cur |= next
                if needUpdate:
                    updateBy.append((state, stateIndex))
            return True
        return False

    def _getNextState(self, handles: Set[Tuple[int, int]]) -> State:
        nextBaseLookaheadByHandle = {}
        for handle in handles:
            rule_num, pos = handle
            handleNext = (rule_num, pos + 1)
            nextBaseLookaheadByHandle[handleNext] = self.curState.lookaheadByHandle[handle]
        nextBaseState = State(lookaheadByHandle=nextBaseLookaheadByHandle)
        return self.stateGenerator(nextBaseState)

    def _processReducableHandles(self, reducableHandles):
        ruleNumsByLookaheadTerminal = self._generateRuleNumsByLookaheadTerminal(reducableHandles)

        for terminal, ruleNums in ruleNumsByLookaheadTerminal.items():
            curColumn = self.tableTerminals[terminal.num]
            transitionType, _ = curColumn[self.curIndex]

            if len(ruleNums) == 1:
                if transitionType == TransitionType.SHIFT:
                    msg = f'Conflict Shift-Reduce: state {self.curIndex} - terminal {terminal.name}'
                    curColumn[self.curIndex] = (TransitionType.BAD, msg)
                else:
                    curColumn[self.curIndex] = (TransitionType.REDUCE, ruleNums[0])
            else:
                msg = f'Conflict Reduce-Reduce: state {self.curIndex} - terminal {terminal.name}'
                curColumn[self.curIndex] = (TransitionType.BAD, msg)

    def _generateRuleNumsByLookaheadTerminal(self, reducableHandles: [(int, int)]) -> dict[Terminal, [int]]:
        res = {}
        for handle in reducableHandles:
            ruleNum, _ = handle
            for terminal in self.curState.getLookahead(handle):
                if terminal not in res:
                    res[terminal] = []
                res[terminal].append(ruleNum)
        return res

    def _append(self, curColumn: [Any], value):
        if self.curIndex < len(curColumn):
            curColumn[self.curIndex] = value
        else:
            curColumn.append(value)
