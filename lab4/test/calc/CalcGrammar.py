from alr import instances
from alr import lexer
from alr import parser
from alr import input_streams


nterminals = None  # for context classes


class _SContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[0])


class EContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[1])


class TContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[2])


class PContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[6])


class LContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[10])


class FContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[13])


class _Rule1Context:
    def __init__(self):
        self.E = []
        self._terminal0 = []
        self.T = []
        self._F3 = []


class _Rule3Context:
    def __init__(self):
        self.E = []
        self.minus = []
        self.T = []
        self._F4 = []


class _Rule5Context:
    def __init__(self):
        self.E = []
        self.T = []
        self._F5 = []


class _Rule7Context:
    def __init__(self):
        self.T = []
        self._terminal2 = []
        self.P = []
        self._F7 = []


class _Rule9Context:
    def __init__(self):
        self.T = []
        self._terminal3 = []
        self.P = []
        self._F8 = []


class _Rule11Context:
    def __init__(self):
        self.T = []
        self.P = []
        self._F9 = []


class _Rule13Context:
    def __init__(self):
        self.P = []
        self.L = []
        self._terminal4 = []
        self._F11 = []


class _Rule15Context:
    def __init__(self):
        self.P = []
        self.L = []
        self._F12 = []


class _Rule17Context:
    def __init__(self):
        self.L = []
        self.minus = []
        self.F = []
        self._F14 = []


class _Rule19Context:
    def __init__(self):
        self.L = []
        self.F = []
        self._F15 = []


class _Rule21Context:
    def __init__(self):
        self.F = []
        self.n = []
        self._F16 = []


class _Rule23Context:
    def __init__(self):
        self.F = []
        self._terminal6 = []
        self.E = []
        self._terminal7 = []
        self._F17 = []


class _F3Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule1Context):
        super().__init__(nterminals[3])
        rctx.E[0].val = rctx.E[1].val + rctx.T[0].val


class _F4Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule3Context):
        super().__init__(nterminals[4])
        rctx.E[0].val = rctx.E[1].val - rctx.T[0].val


class _F5Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule5Context):
        super().__init__(nterminals[5])
        rctx.E[0].val = rctx.T[0].val


class _F7Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule7Context):
        super().__init__(nterminals[7])
        rctx.T[0].val = rctx.T[1].val * rctx.P[0].val


class _F8Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule9Context):
        super().__init__(nterminals[8])
        rctx.T[0].val = rctx.T[1].val // rctx.P[0].val


class _F9Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule11Context):
        super().__init__(nterminals[9])
        rctx.T[0].val = rctx.P[0].val


class _F11Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule13Context):
        super().__init__(nterminals[11])
        rctx.P[0].val = int(rctx.L[0].val ** rctx.P[1].val)


class _F12Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule15Context):
        super().__init__(nterminals[12])
        rctx.P[0].val = rctx.L[0].val


class _F14Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule17Context):
        super().__init__(nterminals[14])
        rctx.L[0].val = - rctx.F[0].val


class _F15Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule19Context):
        super().__init__(nterminals[15])
        rctx.L[0].val =   rctx.F[0].val


class _F16Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule21Context):
        super().__init__(nterminals[16])
        rctx.F[0].val = rctx.n[0].int


class _F17Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule23Context):
        super().__init__(nterminals[17])
        rctx.F[0].val = rctx.E[0].val


terminals = [instances.Terminal("_terminal0", 0, "\+"), instances.Terminal("minus", 1, "-"), instances.Terminal("_terminal2", 2, "\*"), instances.Terminal("_terminal3", 3, "/"), instances.Terminal("_terminal4", 4, "\^"), instances.Terminal("n", 5, "[1-9][0-9]*"), instances.Terminal("_terminal6", 6, "\("), instances.Terminal("_terminal7", 7, "\)")]

skipTerminals = [instances.Terminal("ws", 0, "[ \n\t\r]+")]

nterminals = [instances.Nterminal("_S", 0), instances.Nterminal("E", 1), instances.Nterminal("T", 2), instances.FuncSymbol("_F3", 3), instances.FuncSymbol("_F4", 4), instances.FuncSymbol("_F5", 5), instances.Nterminal("P", 6), instances.FuncSymbol("_F7", 7), instances.FuncSymbol("_F8", 8), instances.FuncSymbol("_F9", 9), instances.Nterminal("L", 10), instances.FuncSymbol("_F11", 11), instances.FuncSymbol("_F12", 12), instances.Nterminal("F", 13), instances.FuncSymbol("_F14", 14), instances.FuncSymbol("_F15", 15), instances.FuncSymbol("_F16", 16), instances.FuncSymbol("_F17", 17)]

rules = [instances.Rule(0, nterminals[0], [nterminals[1]]), instances.Rule(1, nterminals[1], [nterminals[1], terminals[0], nterminals[2], nterminals[3]]), instances.Rule(2, nterminals[3], []), instances.Rule(3, nterminals[1], [nterminals[1], terminals[1], nterminals[2], nterminals[4]]), instances.Rule(4, nterminals[4], []), instances.Rule(5, nterminals[1], [nterminals[2], nterminals[5]]), instances.Rule(6, nterminals[5], []), instances.Rule(7, nterminals[2], [nterminals[2], terminals[2], nterminals[6], nterminals[7]]), instances.Rule(8, nterminals[7], []), instances.Rule(9, nterminals[2], [nterminals[2], terminals[3], nterminals[6], nterminals[8]]), instances.Rule(10, nterminals[8], []), instances.Rule(11, nterminals[2], [nterminals[6], nterminals[9]]), instances.Rule(12, nterminals[9], []), instances.Rule(13, nterminals[6], [nterminals[10], terminals[4], nterminals[6], nterminals[11]]), instances.Rule(14, nterminals[11], []), instances.Rule(15, nterminals[6], [nterminals[10], nterminals[12]]), instances.Rule(16, nterminals[12], []), instances.Rule(17, nterminals[10], [terminals[1], nterminals[13], nterminals[14]]), instances.Rule(18, nterminals[14], []), instances.Rule(19, nterminals[10], [nterminals[13], nterminals[15]]), instances.Rule(20, nterminals[15], []), instances.Rule(21, nterminals[13], [terminals[5], nterminals[16]]), instances.Rule(22, nterminals[16], []), instances.Rule(23, nterminals[13], [terminals[6], nterminals[1], terminals[7], nterminals[17]]), instances.Rule(24, nterminals[17], [])]

nterminals[0].rules = [rules[0]]
nterminals[1].rules = [rules[1], rules[3], rules[5]]
nterminals[2].rules = [rules[7], rules[9], rules[11]]
nterminals[3].rules = [rules[2]]
nterminals[4].rules = [rules[4]]
nterminals[5].rules = [rules[6]]
nterminals[6].rules = [rules[13], rules[15]]
nterminals[7].rules = [rules[8]]
nterminals[8].rules = [rules[10]]
nterminals[9].rules = [rules[12]]
nterminals[10].rules = [rules[17], rules[19]]
nterminals[11].rules = [rules[14]]
nterminals[12].rules = [rules[16]]
nterminals[13].rules = [rules[21], rules[23]]
nterminals[14].rules = [rules[18]]
nterminals[15].rules = [rules[20]]
nterminals[16].rules = [rules[22]]
nterminals[17].rules = [rules[24]]

nterminalConstructors = [_SContext, EContext, TContext, _F3Context, _F4Context, _F5Context, PContext, _F7Context, _F8Context, _F9Context, LContext, _F11Context, _F12Context, FContext, _F14Context, _F15Context, _F16Context, _F17Context]

ruleConstructorByNum = {1: _Rule1Context, 3: _Rule3Context, 5: _Rule5Context, 7: _Rule7Context, 9: _Rule9Context, 11: _Rule11Context, 13: _Rule13Context, 15: _Rule15Context, 17: _Rule17Context, 19: _Rule19Context, 21: _Rule21Context, 23: _Rule23Context}

ruleAndPosByNum = {3: (1, 3), 4: (3, 3), 5: (5, 1), 7: (7, 3), 8: (9, 3), 9: (11, 1), 11: (13, 3), 12: (15, 1), 14: (17, 2), 15: (19, 1), 16: (21, 1), 17: (23, 3)}

table = instances.Table([[instances.TransitionType.BAD, 1, 2, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 3, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 4, instances.TransitionType.BAD, instances.TransitionType.BAD, 5, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 11, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 14, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 15, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 17, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 18, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 19, instances.TransitionType.BAD], [instances.TransitionType.BAD, 20, 2, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 3, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 4, instances.TransitionType.BAD, instances.TransitionType.BAD, 5, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, 21, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 3, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 4, instances.TransitionType.BAD, instances.TransitionType.BAD, 5, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, 22, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 3, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 4, instances.TransitionType.BAD, instances.TransitionType.BAD, 5, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 23, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 4, instances.TransitionType.BAD, instances.TransitionType.BAD, 5, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 24, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 4, instances.TransitionType.BAD, instances.TransitionType.BAD, 5, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 25, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 4, instances.TransitionType.BAD, instances.TransitionType.BAD, 5, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 26, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 28, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 29, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 30, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 31, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 32, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 33], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD]], [[(instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal0'), (instances.TransitionType.SHIFT, 6), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal4'), (instances.TransitionType.SHIFT, 7), (instances.TransitionType.SHIFT, 8), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal7'), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _END')], [(instances.TransitionType.SHIFT, 9), (instances.TransitionType.SHIFT, 10), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal6'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal7'), (instances.TransitionType.REDUCE, 0)], [(instances.TransitionType.REDUCE, 6), (instances.TransitionType.REDUCE, 6), (instances.TransitionType.SHIFT, 12), (instances.TransitionType.SHIFT, 13), (instances.TransitionType.BAD, 'no transition from state 2 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 2 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 2 by terminal _terminal6'), (instances.TransitionType.REDUCE, 6), (instances.TransitionType.REDUCE, 6)], [(instances.TransitionType.REDUCE, 12), (instances.TransitionType.REDUCE, 12), (instances.TransitionType.REDUCE, 12), (instances.TransitionType.REDUCE, 12), (instances.TransitionType.BAD, 'no transition from state 3 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 3 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 3 by terminal _terminal6'), (instances.TransitionType.REDUCE, 12), (instances.TransitionType.REDUCE, 12)], [(instances.TransitionType.REDUCE, 16), (instances.TransitionType.REDUCE, 16), (instances.TransitionType.REDUCE, 16), (instances.TransitionType.REDUCE, 16), (instances.TransitionType.SHIFT, 16), (instances.TransitionType.BAD, 'no transition from state 4 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 4 by terminal _terminal6'), (instances.TransitionType.REDUCE, 16), (instances.TransitionType.REDUCE, 16)], [(instances.TransitionType.REDUCE, 20), (instances.TransitionType.REDUCE, 20), (instances.TransitionType.REDUCE, 20), (instances.TransitionType.REDUCE, 20), (instances.TransitionType.REDUCE, 20), (instances.TransitionType.BAD, 'no transition from state 5 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 5 by terminal _terminal6'), (instances.TransitionType.REDUCE, 20), (instances.TransitionType.REDUCE, 20)], [(instances.TransitionType.BAD, 'no transition from state 6 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 6 by terminal minus'), (instances.TransitionType.BAD, 'no transition from state 6 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 6 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 6 by terminal _terminal4'), (instances.TransitionType.SHIFT, 7), (instances.TransitionType.SHIFT, 8), (instances.TransitionType.BAD, 'no transition from state 6 by terminal _terminal7'), (instances.TransitionType.BAD, 'no transition from state 6 by terminal _END')], [(instances.TransitionType.REDUCE, 22), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.BAD, 'no transition from state 7 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 7 by terminal _terminal6'), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.REDUCE, 22)], [(instances.TransitionType.BAD, 'no transition from state 8 by terminal _terminal0'), (instances.TransitionType.SHIFT, 6), (instances.TransitionType.BAD, 'no transition from state 8 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 8 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 8 by terminal _terminal4'), (instances.TransitionType.SHIFT, 7), (instances.TransitionType.SHIFT, 8), (instances.TransitionType.BAD, 'no transition from state 8 by terminal _terminal7'), (instances.TransitionType.BAD, 'no transition from state 8 by terminal _END')], [(instances.TransitionType.BAD, 'no transition from state 9 by terminal _terminal0'), (instances.TransitionType.SHIFT, 6), (instances.TransitionType.BAD, 'no transition from state 9 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 9 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 9 by terminal _terminal4'), (instances.TransitionType.SHIFT, 7), (instances.TransitionType.SHIFT, 8), (instances.TransitionType.BAD, 'no transition from state 9 by terminal _terminal7'), (instances.TransitionType.BAD, 'no transition from state 9 by terminal _END')], [(instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal0'), (instances.TransitionType.SHIFT, 6), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal4'), (instances.TransitionType.SHIFT, 7), (instances.TransitionType.SHIFT, 8), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal7'), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _END')], [(instances.TransitionType.REDUCE, 5), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 11 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal6'), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.REDUCE, 5)], [(instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal0'), (instances.TransitionType.SHIFT, 6), (instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal4'), (instances.TransitionType.SHIFT, 7), (instances.TransitionType.SHIFT, 8), (instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal7'), (instances.TransitionType.BAD, 'no transition from state 12 by terminal _END')], [(instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal0'), (instances.TransitionType.SHIFT, 6), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal4'), (instances.TransitionType.SHIFT, 7), (instances.TransitionType.SHIFT, 8), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal7'), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _END')], [(instances.TransitionType.REDUCE, 11), (instances.TransitionType.REDUCE, 11), (instances.TransitionType.REDUCE, 11), (instances.TransitionType.REDUCE, 11), (instances.TransitionType.BAD, 'no transition from state 14 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 14 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 14 by terminal _terminal6'), (instances.TransitionType.REDUCE, 11), (instances.TransitionType.REDUCE, 11)], [(instances.TransitionType.REDUCE, 15), (instances.TransitionType.REDUCE, 15), (instances.TransitionType.REDUCE, 15), (instances.TransitionType.REDUCE, 15), (instances.TransitionType.BAD, 'no transition from state 15 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 15 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 15 by terminal _terminal6'), (instances.TransitionType.REDUCE, 15), (instances.TransitionType.REDUCE, 15)], [(instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal0'), (instances.TransitionType.SHIFT, 6), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal4'), (instances.TransitionType.SHIFT, 7), (instances.TransitionType.SHIFT, 8), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal7'), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _END')], [(instances.TransitionType.REDUCE, 19), (instances.TransitionType.REDUCE, 19), (instances.TransitionType.REDUCE, 19), (instances.TransitionType.REDUCE, 19), (instances.TransitionType.REDUCE, 19), (instances.TransitionType.BAD, 'no transition from state 17 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 17 by terminal _terminal6'), (instances.TransitionType.REDUCE, 19), (instances.TransitionType.REDUCE, 19)], [(instances.TransitionType.REDUCE, 18), (instances.TransitionType.REDUCE, 18), (instances.TransitionType.REDUCE, 18), (instances.TransitionType.REDUCE, 18), (instances.TransitionType.REDUCE, 18), (instances.TransitionType.BAD, 'no transition from state 18 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 18 by terminal _terminal6'), (instances.TransitionType.REDUCE, 18), (instances.TransitionType.REDUCE, 18)], [(instances.TransitionType.REDUCE, 21), (instances.TransitionType.REDUCE, 21), (instances.TransitionType.REDUCE, 21), (instances.TransitionType.REDUCE, 21), (instances.TransitionType.REDUCE, 21), (instances.TransitionType.BAD, 'no transition from state 19 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 19 by terminal _terminal6'), (instances.TransitionType.REDUCE, 21), (instances.TransitionType.REDUCE, 21)], [(instances.TransitionType.SHIFT, 9), (instances.TransitionType.SHIFT, 10), (instances.TransitionType.BAD, 'no transition from state 20 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 20 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 20 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 20 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 20 by terminal _terminal6'), (instances.TransitionType.SHIFT, 27), (instances.TransitionType.BAD, 'no transition from state 20 by terminal _END')], [(instances.TransitionType.REDUCE, 2), (instances.TransitionType.REDUCE, 2), (instances.TransitionType.SHIFT, 12), (instances.TransitionType.SHIFT, 13), (instances.TransitionType.BAD, 'no transition from state 21 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 21 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 21 by terminal _terminal6'), (instances.TransitionType.REDUCE, 2), (instances.TransitionType.REDUCE, 2)], [(instances.TransitionType.REDUCE, 4), (instances.TransitionType.REDUCE, 4), (instances.TransitionType.SHIFT, 12), (instances.TransitionType.SHIFT, 13), (instances.TransitionType.BAD, 'no transition from state 22 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 22 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 22 by terminal _terminal6'), (instances.TransitionType.REDUCE, 4), (instances.TransitionType.REDUCE, 4)], [(instances.TransitionType.REDUCE, 8), (instances.TransitionType.REDUCE, 8), (instances.TransitionType.REDUCE, 8), (instances.TransitionType.REDUCE, 8), (instances.TransitionType.BAD, 'no transition from state 23 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 23 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 23 by terminal _terminal6'), (instances.TransitionType.REDUCE, 8), (instances.TransitionType.REDUCE, 8)], [(instances.TransitionType.REDUCE, 10), (instances.TransitionType.REDUCE, 10), (instances.TransitionType.REDUCE, 10), (instances.TransitionType.REDUCE, 10), (instances.TransitionType.BAD, 'no transition from state 24 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 24 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 24 by terminal _terminal6'), (instances.TransitionType.REDUCE, 10), (instances.TransitionType.REDUCE, 10)], [(instances.TransitionType.REDUCE, 14), (instances.TransitionType.REDUCE, 14), (instances.TransitionType.REDUCE, 14), (instances.TransitionType.REDUCE, 14), (instances.TransitionType.BAD, 'no transition from state 25 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 25 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 25 by terminal _terminal6'), (instances.TransitionType.REDUCE, 14), (instances.TransitionType.REDUCE, 14)], [(instances.TransitionType.REDUCE, 17), (instances.TransitionType.REDUCE, 17), (instances.TransitionType.REDUCE, 17), (instances.TransitionType.REDUCE, 17), (instances.TransitionType.REDUCE, 17), (instances.TransitionType.BAD, 'no transition from state 26 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 26 by terminal _terminal6'), (instances.TransitionType.REDUCE, 17), (instances.TransitionType.REDUCE, 17)], [(instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.BAD, 'no transition from state 27 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 27 by terminal _terminal6'), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24)], [(instances.TransitionType.REDUCE, 1), (instances.TransitionType.REDUCE, 1), (instances.TransitionType.BAD, 'no transition from state 28 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 28 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 28 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 28 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 28 by terminal _terminal6'), (instances.TransitionType.REDUCE, 1), (instances.TransitionType.REDUCE, 1)], [(instances.TransitionType.REDUCE, 3), (instances.TransitionType.REDUCE, 3), (instances.TransitionType.BAD, 'no transition from state 29 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 29 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 29 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 29 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 29 by terminal _terminal6'), (instances.TransitionType.REDUCE, 3), (instances.TransitionType.REDUCE, 3)], [(instances.TransitionType.REDUCE, 7), (instances.TransitionType.REDUCE, 7), (instances.TransitionType.REDUCE, 7), (instances.TransitionType.REDUCE, 7), (instances.TransitionType.BAD, 'no transition from state 30 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 30 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 30 by terminal _terminal6'), (instances.TransitionType.REDUCE, 7), (instances.TransitionType.REDUCE, 7)], [(instances.TransitionType.REDUCE, 9), (instances.TransitionType.REDUCE, 9), (instances.TransitionType.REDUCE, 9), (instances.TransitionType.REDUCE, 9), (instances.TransitionType.BAD, 'no transition from state 31 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 31 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 31 by terminal _terminal6'), (instances.TransitionType.REDUCE, 9), (instances.TransitionType.REDUCE, 9)], [(instances.TransitionType.REDUCE, 13), (instances.TransitionType.REDUCE, 13), (instances.TransitionType.REDUCE, 13), (instances.TransitionType.REDUCE, 13), (instances.TransitionType.BAD, 'no transition from state 32 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 32 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 32 by terminal _terminal6'), (instances.TransitionType.REDUCE, 13), (instances.TransitionType.REDUCE, 13)], [(instances.TransitionType.REDUCE, 23), (instances.TransitionType.REDUCE, 23), (instances.TransitionType.REDUCE, 23), (instances.TransitionType.REDUCE, 23), (instances.TransitionType.REDUCE, 23), (instances.TransitionType.BAD, 'no transition from state 33 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 33 by terminal _terminal6'), (instances.TransitionType.REDUCE, 23), (instances.TransitionType.REDUCE, 23)]])


class CalcLexer(lexer.Lexer):
    def __init__(self, inputStream: input_streams.InputStream):
        self._lexer = lexer.lexer(terminals, skipTerminals, inputStream)

    def next(self) -> instances.Token:
        return next(self._lexer)


class CalcParser:
    def __init__(self, calcLexer: CalcLexer):
        self._parser = parser.Parser(nterminals, nterminalConstructors, rules, ruleConstructorByNum, ruleAndPosByNum, table, calcLexer)
        self._parseCnt = 0

    def parse(self, tree: bool = False) -> instances.NterminalContext:
        if self._parseCnt != 0:
            raise parser.ParserException('parser object can parse only once')
        self._parseCnt += 1
        return self._parser.parse(tree)

