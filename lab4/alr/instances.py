from enum import Enum
from typing import Union, Optional, List

import graphviz

_package = "instances"


class TransitionType(Enum):
    SHIFT = 1
    REDUCE = 2
    BAD = 3

    def __repr__(self):
        return _package + "." + super().__str__()


class Terminal:
    def __init__(self, name: str, num: int, regexp: Optional[str] = None):
        self.name = name
        self.num = num
        self.regexp = regexp

    def __repr__(self):
        return f'{_package}.Terminal("{self.name}", {self.num}, "{self.regexp}")'

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


EPS = Terminal("_EPS", -1)

INIT_NTERMINAL_NAME = "_S"
END_TERMINAL_NAME = "_END"

Rule = None


class Nterminal:
    def __init__(self, name: str, num: int, rules: Optional[List[Rule]] = None):
        self.name = name
        self.num = num
        self.rules = [] if rules is None else rules

    def __repr__(self):
        return f'{_package}.Nterminal("{self.name}", {self.num})'

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


class TranslationSymbol(Nterminal):
    def __init__(self, name: str, num: int, rules: Optional[List[Rule]] = None):
        super().__init__(name, num, rules)

    def __repr__(self):
        val = super().__repr__()
        val = val[val.find('('):]
        return _package + "." + type(self).__name__ + val


class ConstructorSymbol(TranslationSymbol):
    def __init__(self, name: str, num: int, rules: Optional[List[Rule]] = None):
        super().__init__(name, num, rules)


class FuncSymbol(TranslationSymbol):
    def __init__(self, name: str, num: int, rules: Optional[List[Rule]] = None):
        super().__init__(name, num, rules)


class Rule:
    def __init__(self, num: int, left: Nterminal, right: [Union[Nterminal, Terminal]]):
        self.num = num
        self.left = left
        self.right = right

    def __repr__(self):
        left_str = f'nterminals[{self.left.num}]'
        right = []
        for el in self.right:
            kind = "terminals" if isinstance(el, Terminal) else "nterminals"
            right.append(f'{kind}[{el.num}]')
        return f'{_package}.Rule({self.num}, {left_str}, [{", ".join(right)}])'

    def __hash__(self):
        return self.num

    def __eq__(self, other):
        return self.num == other.num


class ContextObject:
    def _name(self) -> str:
        pass

    def _isTranslationSymbol(self) -> bool:
        pass

    def getVertexName(self) -> str:
        pass


class Token(ContextObject):
    def __init__(self, terminal: Terminal, start: int, end: int, source: str):
        self._val: Optional[str] = None
        self._int: Optional[int] = None
        self.terminal = terminal
        self.start = start
        self.end = end
        self.source = source

    def _name(self) -> str:
        return self.terminal.name

    def _isTranslationSymbol(self) -> bool:
        return False

    def getVertexName(self) -> str:
        return self.val

    def __repr__(self):
        return f"Token({self.terminal}, {self.start}, {self.end})"

    @property
    def val(self):
        if self._val is None:
            self._val = self.source[self.start: self.end]
        return self._val

    @val.setter
    def val(self, value):
        raise ValueError("Can not update val attribute")

    @property
    def int(self):
        if self._int is None:
            self._int = int(self.val)
        return self._int

    @int.setter
    def int(self, value):
        raise ValueError("Can not update int attribute")


class NterminalContext(ContextObject):
    def __init__(self, nterminal: Nterminal):
        self._nterminal = nterminal
        self._children: Optional[List[ContextObject]] = None

    def _name(self) -> str:
        return self._nterminal.name

    def _isTranslationSymbol(self) -> bool:
        return isinstance(self._nterminal, TranslationSymbol)

    def _add(self, child):
        if self._children is None:
            self._children = []
        self._children.append(child)

    def render(self, fileName: str = 'parse-tree'):
        dot = graphviz.Digraph(name=f'Parse tree')
        dot.node("0", self._findSource(), shape='rectangle', color='red')
        dot.node("1", self.getVertexName())
        dot.edge("0", "1", color='white')
        self._toDot(dot, [1], "1")
        dot.render(fileName, view=True, cleanup=True)

    def _toDot(self, dot, n, curStr):
        cnt = 0
        for child in self._children:
            if child._isTranslationSymbol():
                continue
            cnt += 1
            n[0] += 1
            childStr = str(n[0])
            if isinstance(child, Token):
                color = 'blue'
                down = False
            else:
                color = 'black'
                down = True
            dot.node(childStr, child.getVertexName(), color=color)
            dot.edge(curStr, childStr)
            if down:
                child._toDot(dot, n, childStr)
        if cnt == 0:
            n[0] += 1
            childStr = str(n[0])
            dot.node(childStr, "eps", color='dodgerblue')
            dot.edge(curStr, childStr)

    def getVertexName(self) -> str:
        name = [self._name()]
        for attrName, attrValue in self.__dict__.items():
            if attrName[0] == '_':
                continue
            name.append(f'{attrName} : {attrValue}')
        return '\n'.join(name)

    def _findSource(self):
        if self._children is None:
            return None
        for child in self._children:
            if isinstance(child, Token):
                return child.source
            elif isinstance(child, NterminalContext):
                res = child._findSource()
                if res:
                    return res


class Marker:
    def __init__(self, parentCtx: NterminalContext, rctx, lastPos: int):
        self.parentCtx = parentCtx
        self.rctx = rctx
        self.lastPos = lastPos


class Table:
    def __init__(self, nterminals: [[Union[int, TransitionType]]], terminals: [[(TransitionType, Union[str, int])]]):
        self.nterminals = nterminals
        self.terminals = terminals

    def __repr__(self):
        return _package + f".Table({self.nterminals}, {self.terminals})"
