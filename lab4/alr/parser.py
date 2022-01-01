from alr.instances import Table, Nterminal, Rule, NterminalContext, TransitionType, TranslationSymbol, \
    Marker, ContextObject, ConstructorSymbol, FuncSymbol

from alr.lexer import Lexer


class ParserException(Exception):
    pass


class Parser:
    def __init__(self,
                 nterminals: [Nterminal], nterminalConstructors,
                 rules: [Rule], ruleConstructorByNum,
                 ruleAndPosByNum: dict[int, (int, int)],
                 table: Table,
                 lexer: Lexer):
        self.nterminals = nterminals
        self.nterminalConstructors = nterminalConstructors
        self.rules = rules
        self.ruleConstructorByNum = ruleConstructorByNum
        self.ruleAndPosByNum = ruleAndPosByNum
        self.table = table
        self.lexer = lexer

        self.curState = 0
        self.curToken = None
        self.stack = [0]
        self.markerPointers = []

    def parse(self, tree: bool) -> NterminalContext:
        self.curToken = self.lexer.next()
        while True:
            transitionType, val = self.table.terminals[self.curState][self.curToken.terminal.num]
            if transitionType == TransitionType.BAD:
                exceptionMsg = val
                raise ParserException(exceptionMsg)
            elif transitionType == TransitionType.SHIFT:
                self._changeState(self.curToken, nextState=val)
                self.curToken = self.lexer.next()
            elif transitionType == TransitionType.REDUCE:
                reduceRule = self.rules[val]
                if isinstance(reduceRule.left, TranslationSymbol):
                    self._reduceTranslationSymbolContext(reduceRule)
                else:
                    markerIndex = len(self.stack) - 2 * len(reduceRule.right) - 1
                    curCtx, wasMarker = self._initNterminalCtx(markerIndex, reduceRule)

                    if tree or curCtx._nterminal.name == "_S":
                        self._buildTree(curCtx, markerIndex)

                    self._clearStack(markerIndex, wasMarker)

                    if curCtx._nterminal.name == "_S":
                        return curCtx._children[0]

                    nextState = self.table.nterminals[self._findClosestState()][reduceRule.left.num]
                    self._changeState(curCtx, nextState)

    def _changeState(self, ctx: ContextObject, nextState):
        if nextState is TransitionType.BAD:
            raise ParserException(f'Can not change state from {self.curState} to {nextState}')
        self.stack.append(ctx)
        self.stack.append(nextState)
        self.curState = nextState

    def _reduceTranslationSymbolContext(self, reduceRule):
        cur = reduceRule.left
        curNum = reduceRule.left.num

        parentRuleNum, translationSymbolIndex = self.ruleAndPosByNum[curNum]
        expectedMarkerIndex = len(self.stack) - 1 - 2 * translationSymbolIndex

        marker, markerIndex = self._initMarker(expectedMarkerIndex, parentRuleNum)
        self._updateMarkerRuleContext(marker, markerIndex)
        marker.lastPos = translationSymbolIndex

        nextState = self.table.nterminals[self._findClosestState()][curNum]

        if isinstance(cur, FuncSymbol):
            ctx = self.nterminalConstructors[curNum](marker.rctx)
            self._changeState(ctx, nextState)
        elif isinstance(cur, ConstructorSymbol):
            parentNterminal = self.rules[parentRuleNum].right[translationSymbolIndex + 1]
            parent = self.nterminalConstructors[parentNterminal.num]()
            ctx = self.nterminalConstructors[reduceRule.left.num](parent, marker.rctx)
            self._changeState(ctx, nextState)
            self.stack.append(Marker(parent, None, 0))
            self.markerPointers.append(len(self.stack) - 1)

    def _initMarker(self, expectedMarkerIndex, parentRuleNterminal):
        if not self.markerPointers or self.markerPointers[-1] != expectedMarkerIndex:
            parentNterminal = self.rules[parentRuleNterminal].left
            parentCtx = self.nterminalConstructors[parentNterminal.num]()

            rctx = self._initRctx(parentCtx, parentRuleNterminal)

            marker = Marker(parentCtx, rctx, 0)
            markerIndex = expectedMarkerIndex + 1

            self.stack.insert(markerIndex, marker)
            self.markerPointers.append(markerIndex)
        else:
            marker = self.stack[expectedMarkerIndex]
            markerIndex = expectedMarkerIndex
            if marker.rctx is None:
                marker.rctx = self._initRctx(marker.parentCtx, parentRuleNterminal)
        return marker, markerIndex

    def _initRctx(self, parentCtx, parentRuleNum):
        rctx = self.ruleConstructorByNum[parentRuleNum]()
        getattr(rctx, parentCtx._name()).append(parentCtx)
        return rctx

    def _updateMarkerRuleContext(self, marker, marker_index):
        ctxs = (self.stack[i] for i in range(marker_index + 1 + marker.lastPos * 2, len(self.stack), 2))
        for ctx in ctxs:
            if not ctx._isTranslationSymbol():
                getattr(marker.rctx, ctx._name()).append(ctx)

    def _initNterminalCtx(self, markerIndex, reduceRule):
        if not self.markerPointers or self.markerPointers[-1] != markerIndex:
            curCtx = self.nterminalConstructors[reduceRule.left.num]()
            wasMarker = False
        else:
            curCtx = self.stack[markerIndex].parentCtx
            wasMarker = True
        return curCtx, wasMarker

    def _buildTree(self, curCtx, markerIndex):
        for i in range(markerIndex + 1, len(self.stack), 2):
            curCtx._add(self.stack[i])

    def _clearStack(self, markerIndex, wasMarker):
        for i in range(len(self.stack) - markerIndex - 1):
            self.stack.pop()
        if wasMarker:
            self.stack.pop()
            self.markerPointers.pop()

    def _findClosestState(self):
        last = self.stack[-1]
        if isinstance(last, Marker):
            return self.stack[-2]
        else:
            return last
