from enum import Enum, auto
import graphviz


class ParseException(Exception):
    def __init__(self, pos, char, expected=None, info=None):
        log = f'Incorrect input: pos={pos}, char={char}'
        if expected is not None:
            log += f', expected={expected}'
        if info is not None:
            log += f', info={info}'
        super().__init__(log)


class Token(Enum):
    OR = auto()
    STAR = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    CHAR = auto()
    END = auto()


def lexical_analyzer(input_str):
    for pos, char in enumerate(input_str):
        if char.isspace():
            continue

        token = None
        if char == "|":
            token = Token.OR
        elif char == "*":
            token = Token.STAR
        elif char == "(":
            token = Token.LBRACKET
        elif char == ")":
            token = Token.RBRACKET
        elif "a" <= char <= "z":
            token = Token.CHAR

        if token is None:
            raise ParseException(pos=pos, char=char)

        yield token, char, pos
    yield Token.END, None, len(input_str)


class Tree:
    def __init__(self, value, *children):
        self.value = value
        self.children = children

    def __str__(self):
        chars = []
        self._str(chars)
        return "".join(chars)

    def is_terminal(self):
        return not len(self.children) and \
               not self.value[0].isupper()

    def _str(self, chars):
        if self.is_terminal():
            chars.append(self.value)
        for child in self.children:
            child._str(chars)

    def to_dot(self):
        dot = graphviz.Digraph(name=f'Syntax tree')
        dot.node("0", str(self), shape='rectangle', color='red')
        dot.node("1", self.value)
        dot.edge("0", "1", color='white')
        self._to_dot(dot, [1], "1")
        return dot

    def _to_dot(self, dot, n, cur_str):
        for child in self.children:
            n[0] += 1
            child_str = str(n[0])
            dot.node(
                child_str,
                child.value,
                color=('blue' if child.is_terminal() else 'black')
            )
            dot.edge(cur_str, child_str)
            child._to_dot(dot, n, child_str)


class Parser:
    def parse(self, input_str, modification=False):
        self._lexical_analyzer = lexical_analyzer(input_str)
        self._modification = modification
        self._next_token()
        return self._s()

    def _next_token(self):
        token, char, pos = next(self._lexical_analyzer)
        self._token = token
        self._char = char
        self._pos = pos

    def _raise_exception(self, info=None, expected=None):
        raise ParseException(
            pos=self._pos,
            char=self._char,
            info=info,
            expected=expected
        )

    def _s(self):
        if self._token == Token.END:
            return Tree("S")
        return Tree("S", self._or())

    def _or(self):
        return Tree("Or", self._and(), self._or_prime())

    def _or_prime(self):
        if self._token == Token.OR:
            self._next_token()
            return Tree("Or'", Tree("|"), self._or())
        return Tree("Or'")

    def _and(self):
        return Tree("And", self._st(), self._and_prime())

    def _and_prime(self):
        if self._token in (Token.END, Token.RBRACKET, Token.OR):
            return Tree("And'")
        return Tree("And'", self._and())

    def _st(self):
        return Tree("St", self._c(), self._st_prime())

    def _st_prime(self):
        if self._token == Token.STAR:
            self._next_token()
            if self._modification:
                return Tree("St'", Tree("*"))
            else:
                return Tree("St'", Tree("*"), self._st_prime())
        return Tree("St'")

    def _c(self):
        if self._token == Token.LBRACKET:
            self._next_token()
            subtree = self._or()
            if self._token != Token.RBRACKET:
                self._raise_exception(expected="Right bracket")
            self._next_token()
            return Tree("C", Tree("("), subtree, Tree(")"))
        elif self._token == Token.CHAR:
            res = Tree("C", Tree(self._char))
            self._next_token()
            return res
        self._raise_exception(info="Unknown symbol")
