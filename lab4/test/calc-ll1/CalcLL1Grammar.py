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


class E_Context(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[3])
        self.acc = None


class FContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[11])


class T_Context(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[12])
        self.acc = None


class _Rule1Context:
    def __init__(self):
        self.E = []
        self.T = []
        self._C4 = []
        self.E_ = []
        self._F5 = []


class _Rule4Context:
    def __init__(self):
        self.E_ = []
        self._terminal0 = []
        self.T = []
        self._C6 = []
        self._F7 = []


class _Rule7Context:
    def __init__(self):
        self.E_ = []
        self._terminal1 = []
        self.T = []
        self._C8 = []
        self._F9 = []


class _Rule12Context:
    def __init__(self):
        self.T = []
        self.F = []
        self._C13 = []
        self.T_ = []
        self._F14 = []


class _Rule15Context:
    def __init__(self):
        self.T_ = []
        self._terminal2 = []
        self.F = []
        self._C15 = []
        self._F16 = []


class _Rule18Context:
    def __init__(self):
        self.T_ = []
        self._terminal3 = []
        self.F = []
        self._C17 = []
        self._F18 = []


class _Rule10Context:
    def __init__(self):
        self.E_ = []
        self._F10 = []


class _Rule21Context:
    def __init__(self):
        self.T_ = []
        self._F19 = []


class _Rule23Context:
    def __init__(self):
        self.F = []
        self._terminal4 = []
        self.E = []
        self._terminal5 = []
        self._F20 = []


class _Rule25Context:
    def __init__(self):
        self.F = []
        self.n = []
        self._F21 = []


class _C4Context(instances.NterminalContext):
    def __init__(self, parent: E_Context, rctx: _Rule1Context):
        super().__init__(nterminals[4])
        parent.acc = rctx.T[0].val


class _C6Context(instances.NterminalContext):
    def __init__(self, parent: E_Context, rctx: _Rule4Context):
        super().__init__(nterminals[6])
        parent.acc = rctx.E_[0].acc + rctx.T[0].val


class _C8Context(instances.NterminalContext):
    def __init__(self, parent: E_Context, rctx: _Rule7Context):
        super().__init__(nterminals[8])
        parent.acc = rctx.E_[0].acc - rctx.T[0].val


class _C13Context(instances.NterminalContext):
    def __init__(self, parent: T_Context, rctx: _Rule12Context):
        super().__init__(nterminals[13])
        parent.acc = rctx.F[0].val


class _C15Context(instances.NterminalContext):
    def __init__(self, parent: T_Context, rctx: _Rule15Context):
        super().__init__(nterminals[15])
        parent.acc = rctx.T_[0].acc * rctx.F[0].val


class _C17Context(instances.NterminalContext):
    def __init__(self, parent: T_Context, rctx: _Rule18Context):
        super().__init__(nterminals[17])
        parent.acc = rctx.T_[0].acc // rctx.F[0].val


class _F5Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule1Context):
        super().__init__(nterminals[5])
        rctx.E[0].val = rctx.E_[0].val


class _F7Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule4Context):
        super().__init__(nterminals[7])
        rctx.E_[0].val = rctx.E_[1].val


class _F9Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule7Context):
        super().__init__(nterminals[9])
        rctx.E_[0].val = rctx.E_[1].val


class _F10Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule10Context):
        super().__init__(nterminals[10])
        rctx.E_[0].val = rctx.E_[0].acc


class _F14Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule12Context):
        super().__init__(nterminals[14])
        rctx.T[0].val = rctx.T_[0].val


class _F16Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule15Context):
        super().__init__(nterminals[16])
        rctx.T_[0].val = rctx.T_[1].val


class _F18Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule18Context):
        super().__init__(nterminals[18])
        rctx.T_[0].val = rctx.T_[1].val


class _F19Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule21Context):
        super().__init__(nterminals[19])
        rctx.T_[0].val = rctx.T_[0].acc


class _F20Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule23Context):
        super().__init__(nterminals[20])
        rctx.F[0].val = rctx.E[0].val


class _F21Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule25Context):
        super().__init__(nterminals[21])
        rctx.F[0].val = rctx.n[0].int


terminals = [instances.Terminal("_terminal0", 0, "\+"), instances.Terminal("_terminal1", 1, "-"), instances.Terminal("_terminal2", 2, "\*"), instances.Terminal("_terminal3", 3, "/"), instances.Terminal("_terminal4", 4, "\("), instances.Terminal("_terminal5", 5, "\)"), instances.Terminal("n", 6, "[1-9][0-9]*")]

skipTerminals = [instances.Terminal("ws", 0, "[ \n\t\r]+")]

nterminals = [instances.Nterminal("_S", 0), instances.Nterminal("E", 1), instances.Nterminal("T", 2), instances.Nterminal("E_", 3), instances.ConstructorSymbol("_C4", 4), instances.FuncSymbol("_F5", 5), instances.ConstructorSymbol("_C6", 6), instances.FuncSymbol("_F7", 7), instances.ConstructorSymbol("_C8", 8), instances.FuncSymbol("_F9", 9), instances.FuncSymbol("_F10", 10), instances.Nterminal("F", 11), instances.Nterminal("T_", 12), instances.ConstructorSymbol("_C13", 13), instances.FuncSymbol("_F14", 14), instances.ConstructorSymbol("_C15", 15), instances.FuncSymbol("_F16", 16), instances.ConstructorSymbol("_C17", 17), instances.FuncSymbol("_F18", 18), instances.FuncSymbol("_F19", 19), instances.FuncSymbol("_F20", 20), instances.FuncSymbol("_F21", 21)]

rules = [instances.Rule(0, nterminals[0], [nterminals[1]]), instances.Rule(1, nterminals[1], [nterminals[2], nterminals[4], nterminals[3], nterminals[5]]), instances.Rule(2, nterminals[4], []), instances.Rule(3, nterminals[5], []), instances.Rule(4, nterminals[3], [terminals[0], nterminals[2], nterminals[6], nterminals[3], nterminals[7]]), instances.Rule(5, nterminals[6], []), instances.Rule(6, nterminals[7], []), instances.Rule(7, nterminals[3], [terminals[1], nterminals[2], nterminals[8], nterminals[3], nterminals[9]]), instances.Rule(8, nterminals[8], []), instances.Rule(9, nterminals[9], []), instances.Rule(10, nterminals[3], [nterminals[10]]), instances.Rule(11, nterminals[10], []), instances.Rule(12, nterminals[2], [nterminals[11], nterminals[13], nterminals[12], nterminals[14]]), instances.Rule(13, nterminals[13], []), instances.Rule(14, nterminals[14], []), instances.Rule(15, nterminals[12], [terminals[2], nterminals[11], nterminals[15], nterminals[12], nterminals[16]]), instances.Rule(16, nterminals[15], []), instances.Rule(17, nterminals[16], []), instances.Rule(18, nterminals[12], [terminals[3], nterminals[11], nterminals[17], nterminals[12], nterminals[18]]), instances.Rule(19, nterminals[17], []), instances.Rule(20, nterminals[18], []), instances.Rule(21, nterminals[12], [nterminals[19]]), instances.Rule(22, nterminals[19], []), instances.Rule(23, nterminals[11], [terminals[4], nterminals[1], terminals[5], nterminals[20]]), instances.Rule(24, nterminals[20], []), instances.Rule(25, nterminals[11], [terminals[6], nterminals[21]]), instances.Rule(26, nterminals[21], [])]

nterminals[0].rules = [rules[0]]
nterminals[1].rules = [rules[1]]
nterminals[2].rules = [rules[12]]
nterminals[3].rules = [rules[4], rules[7], rules[10]]
nterminals[4].rules = [rules[2]]
nterminals[5].rules = [rules[3]]
nterminals[6].rules = [rules[5]]
nterminals[7].rules = [rules[6]]
nterminals[8].rules = [rules[8]]
nterminals[9].rules = [rules[9]]
nterminals[10].rules = [rules[11]]
nterminals[11].rules = [rules[23], rules[25]]
nterminals[12].rules = [rules[15], rules[18], rules[21]]
nterminals[13].rules = [rules[13]]
nterminals[14].rules = [rules[14]]
nterminals[15].rules = [rules[16]]
nterminals[16].rules = [rules[17]]
nterminals[17].rules = [rules[19]]
nterminals[18].rules = [rules[20]]
nterminals[19].rules = [rules[22]]
nterminals[20].rules = [rules[24]]
nterminals[21].rules = [rules[26]]

nterminalConstructors = [_SContext, EContext, TContext, E_Context, _C4Context, _F5Context, _C6Context, _F7Context, _C8Context, _F9Context, _F10Context, FContext, T_Context, _C13Context, _F14Context, _C15Context, _F16Context, _C17Context, _F18Context, _F19Context, _F20Context, _F21Context]

ruleConstructorByNum = {1: _Rule1Context, 4: _Rule4Context, 7: _Rule7Context, 12: _Rule12Context, 15: _Rule15Context, 18: _Rule18Context, 10: _Rule10Context, 21: _Rule21Context, 23: _Rule23Context, 25: _Rule25Context}

ruleAndPosByNum = {4: (1, 1), 5: (1, 3), 6: (4, 2), 7: (4, 4), 8: (7, 2), 9: (7, 4), 10: (10, 0), 13: (12, 1), 14: (12, 3), 15: (15, 2), 16: (15, 4), 17: (18, 2), 18: (18, 4), 19: (21, 0), 20: (23, 3), 21: (25, 1)}

table = instances.Table([[instances.TransitionType.BAD, 1, 2, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 3, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 6, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 7, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, 8, 2, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 3, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 9], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 10, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 11, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 14, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 15, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 19, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, 20, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 3, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, 21, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 3, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 22, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 23, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 24, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 25, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 26, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 27, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 28, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 29, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 30, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 11, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 31, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 11, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 32, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 15, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 33, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 15, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 34, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 35, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 36, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 37, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD]], [[(instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal3'), (instances.TransitionType.SHIFT, 4), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal5'), (instances.TransitionType.SHIFT, 5), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _END')], [(instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal4'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal5'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal n'), (instances.TransitionType.REDUCE, 0)], [(instances.TransitionType.REDUCE, 2), (instances.TransitionType.REDUCE, 2), (instances.TransitionType.BAD, 'no transition from state 2 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 2 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 2 by terminal _terminal4'), (instances.TransitionType.REDUCE, 2), (instances.TransitionType.BAD, 'no transition from state 2 by terminal n'), (instances.TransitionType.REDUCE, 2)], [(instances.TransitionType.REDUCE, 13), (instances.TransitionType.REDUCE, 13), (instances.TransitionType.REDUCE, 13), (instances.TransitionType.REDUCE, 13), (instances.TransitionType.BAD, 'no transition from state 3 by terminal _terminal4'), (instances.TransitionType.REDUCE, 13), (instances.TransitionType.BAD, 'no transition from state 3 by terminal n'), (instances.TransitionType.REDUCE, 13)], [(instances.TransitionType.BAD, 'no transition from state 4 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 4 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 4 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 4 by terminal _terminal3'), (instances.TransitionType.SHIFT, 4), (instances.TransitionType.BAD, 'no transition from state 4 by terminal _terminal5'), (instances.TransitionType.SHIFT, 5), (instances.TransitionType.BAD, 'no transition from state 4 by terminal _END')], [(instances.TransitionType.REDUCE, 26), (instances.TransitionType.REDUCE, 26), (instances.TransitionType.REDUCE, 26), (instances.TransitionType.REDUCE, 26), (instances.TransitionType.BAD, 'no transition from state 5 by terminal _terminal4'), (instances.TransitionType.REDUCE, 26), (instances.TransitionType.BAD, 'no transition from state 5 by terminal n'), (instances.TransitionType.REDUCE, 26)], [(instances.TransitionType.SHIFT, 12), (instances.TransitionType.SHIFT, 13), (instances.TransitionType.BAD, 'no transition from state 6 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 6 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 6 by terminal _terminal4'), (instances.TransitionType.REDUCE, 11), (instances.TransitionType.BAD, 'no transition from state 6 by terminal n'), (instances.TransitionType.REDUCE, 11)], [(instances.TransitionType.REDUCE, 22), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.SHIFT, 16), (instances.TransitionType.SHIFT, 17), (instances.TransitionType.BAD, 'no transition from state 7 by terminal _terminal4'), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.BAD, 'no transition from state 7 by terminal n'), (instances.TransitionType.REDUCE, 22)], [(instances.TransitionType.BAD, 'no transition from state 8 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 8 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 8 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 8 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 8 by terminal _terminal4'), (instances.TransitionType.SHIFT, 18), (instances.TransitionType.BAD, 'no transition from state 8 by terminal n'), (instances.TransitionType.BAD, 'no transition from state 8 by terminal _END')], [(instances.TransitionType.REDUCE, 25), (instances.TransitionType.REDUCE, 25), (instances.TransitionType.REDUCE, 25), (instances.TransitionType.REDUCE, 25), (instances.TransitionType.BAD, 'no transition from state 9 by terminal _terminal4'), (instances.TransitionType.REDUCE, 25), (instances.TransitionType.BAD, 'no transition from state 9 by terminal n'), (instances.TransitionType.REDUCE, 25)], [(instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal4'), (instances.TransitionType.REDUCE, 3), (instances.TransitionType.BAD, 'no transition from state 10 by terminal n'), (instances.TransitionType.REDUCE, 3)], [(instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal4'), (instances.TransitionType.REDUCE, 10), (instances.TransitionType.BAD, 'no transition from state 11 by terminal n'), (instances.TransitionType.REDUCE, 10)], [(instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal3'), (instances.TransitionType.SHIFT, 4), (instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal5'), (instances.TransitionType.SHIFT, 5), (instances.TransitionType.BAD, 'no transition from state 12 by terminal _END')], [(instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal3'), (instances.TransitionType.SHIFT, 4), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal5'), (instances.TransitionType.SHIFT, 5), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _END')], [(instances.TransitionType.REDUCE, 14), (instances.TransitionType.REDUCE, 14), (instances.TransitionType.BAD, 'no transition from state 14 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 14 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 14 by terminal _terminal4'), (instances.TransitionType.REDUCE, 14), (instances.TransitionType.BAD, 'no transition from state 14 by terminal n'), (instances.TransitionType.REDUCE, 14)], [(instances.TransitionType.REDUCE, 21), (instances.TransitionType.REDUCE, 21), (instances.TransitionType.BAD, 'no transition from state 15 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 15 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 15 by terminal _terminal4'), (instances.TransitionType.REDUCE, 21), (instances.TransitionType.BAD, 'no transition from state 15 by terminal n'), (instances.TransitionType.REDUCE, 21)], [(instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal3'), (instances.TransitionType.SHIFT, 4), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal5'), (instances.TransitionType.SHIFT, 5), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _END')], [(instances.TransitionType.BAD, 'no transition from state 17 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 17 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 17 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 17 by terminal _terminal3'), (instances.TransitionType.SHIFT, 4), (instances.TransitionType.BAD, 'no transition from state 17 by terminal _terminal5'), (instances.TransitionType.SHIFT, 5), (instances.TransitionType.BAD, 'no transition from state 17 by terminal _END')], [(instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.BAD, 'no transition from state 18 by terminal _terminal4'), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.BAD, 'no transition from state 18 by terminal n'), (instances.TransitionType.REDUCE, 24)], [(instances.TransitionType.BAD, 'no transition from state 19 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 19 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 19 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 19 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 19 by terminal _terminal4'), (instances.TransitionType.REDUCE, 1), (instances.TransitionType.BAD, 'no transition from state 19 by terminal n'), (instances.TransitionType.REDUCE, 1)], [(instances.TransitionType.REDUCE, 5), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.BAD, 'no transition from state 20 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 20 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 20 by terminal _terminal4'), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.BAD, 'no transition from state 20 by terminal n'), (instances.TransitionType.REDUCE, 5)], [(instances.TransitionType.REDUCE, 8), (instances.TransitionType.REDUCE, 8), (instances.TransitionType.BAD, 'no transition from state 21 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 21 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 21 by terminal _terminal4'), (instances.TransitionType.REDUCE, 8), (instances.TransitionType.BAD, 'no transition from state 21 by terminal n'), (instances.TransitionType.REDUCE, 8)], [(instances.TransitionType.REDUCE, 12), (instances.TransitionType.REDUCE, 12), (instances.TransitionType.BAD, 'no transition from state 22 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 22 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 22 by terminal _terminal4'), (instances.TransitionType.REDUCE, 12), (instances.TransitionType.BAD, 'no transition from state 22 by terminal n'), (instances.TransitionType.REDUCE, 12)], [(instances.TransitionType.REDUCE, 16), (instances.TransitionType.REDUCE, 16), (instances.TransitionType.REDUCE, 16), (instances.TransitionType.REDUCE, 16), (instances.TransitionType.BAD, 'no transition from state 23 by terminal _terminal4'), (instances.TransitionType.REDUCE, 16), (instances.TransitionType.BAD, 'no transition from state 23 by terminal n'), (instances.TransitionType.REDUCE, 16)], [(instances.TransitionType.REDUCE, 19), (instances.TransitionType.REDUCE, 19), (instances.TransitionType.REDUCE, 19), (instances.TransitionType.REDUCE, 19), (instances.TransitionType.BAD, 'no transition from state 24 by terminal _terminal4'), (instances.TransitionType.REDUCE, 19), (instances.TransitionType.BAD, 'no transition from state 24 by terminal n'), (instances.TransitionType.REDUCE, 19)], [(instances.TransitionType.REDUCE, 23), (instances.TransitionType.REDUCE, 23), (instances.TransitionType.REDUCE, 23), (instances.TransitionType.REDUCE, 23), (instances.TransitionType.BAD, 'no transition from state 25 by terminal _terminal4'), (instances.TransitionType.REDUCE, 23), (instances.TransitionType.BAD, 'no transition from state 25 by terminal n'), (instances.TransitionType.REDUCE, 23)], [(instances.TransitionType.SHIFT, 12), (instances.TransitionType.SHIFT, 13), (instances.TransitionType.BAD, 'no transition from state 26 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 26 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 26 by terminal _terminal4'), (instances.TransitionType.REDUCE, 11), (instances.TransitionType.BAD, 'no transition from state 26 by terminal n'), (instances.TransitionType.REDUCE, 11)], [(instances.TransitionType.SHIFT, 12), (instances.TransitionType.SHIFT, 13), (instances.TransitionType.BAD, 'no transition from state 27 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 27 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 27 by terminal _terminal4'), (instances.TransitionType.REDUCE, 11), (instances.TransitionType.BAD, 'no transition from state 27 by terminal n'), (instances.TransitionType.REDUCE, 11)], [(instances.TransitionType.REDUCE, 22), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.SHIFT, 16), (instances.TransitionType.SHIFT, 17), (instances.TransitionType.BAD, 'no transition from state 28 by terminal _terminal4'), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.BAD, 'no transition from state 28 by terminal n'), (instances.TransitionType.REDUCE, 22)], [(instances.TransitionType.REDUCE, 22), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.SHIFT, 16), (instances.TransitionType.SHIFT, 17), (instances.TransitionType.BAD, 'no transition from state 29 by terminal _terminal4'), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.BAD, 'no transition from state 29 by terminal n'), (instances.TransitionType.REDUCE, 22)], [(instances.TransitionType.BAD, 'no transition from state 30 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 30 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 30 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 30 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 30 by terminal _terminal4'), (instances.TransitionType.REDUCE, 6), (instances.TransitionType.BAD, 'no transition from state 30 by terminal n'), (instances.TransitionType.REDUCE, 6)], [(instances.TransitionType.BAD, 'no transition from state 31 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 31 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 31 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 31 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 31 by terminal _terminal4'), (instances.TransitionType.REDUCE, 9), (instances.TransitionType.BAD, 'no transition from state 31 by terminal n'), (instances.TransitionType.REDUCE, 9)], [(instances.TransitionType.REDUCE, 17), (instances.TransitionType.REDUCE, 17), (instances.TransitionType.BAD, 'no transition from state 32 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 32 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 32 by terminal _terminal4'), (instances.TransitionType.REDUCE, 17), (instances.TransitionType.BAD, 'no transition from state 32 by terminal n'), (instances.TransitionType.REDUCE, 17)], [(instances.TransitionType.REDUCE, 20), (instances.TransitionType.REDUCE, 20), (instances.TransitionType.BAD, 'no transition from state 33 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 33 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 33 by terminal _terminal4'), (instances.TransitionType.REDUCE, 20), (instances.TransitionType.BAD, 'no transition from state 33 by terminal n'), (instances.TransitionType.REDUCE, 20)], [(instances.TransitionType.BAD, 'no transition from state 34 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 34 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 34 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 34 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 34 by terminal _terminal4'), (instances.TransitionType.REDUCE, 4), (instances.TransitionType.BAD, 'no transition from state 34 by terminal n'), (instances.TransitionType.REDUCE, 4)], [(instances.TransitionType.BAD, 'no transition from state 35 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 35 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 35 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 35 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 35 by terminal _terminal4'), (instances.TransitionType.REDUCE, 7), (instances.TransitionType.BAD, 'no transition from state 35 by terminal n'), (instances.TransitionType.REDUCE, 7)], [(instances.TransitionType.REDUCE, 15), (instances.TransitionType.REDUCE, 15), (instances.TransitionType.BAD, 'no transition from state 36 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 36 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 36 by terminal _terminal4'), (instances.TransitionType.REDUCE, 15), (instances.TransitionType.BAD, 'no transition from state 36 by terminal n'), (instances.TransitionType.REDUCE, 15)], [(instances.TransitionType.REDUCE, 18), (instances.TransitionType.REDUCE, 18), (instances.TransitionType.BAD, 'no transition from state 37 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 37 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 37 by terminal _terminal4'), (instances.TransitionType.REDUCE, 18), (instances.TransitionType.BAD, 'no transition from state 37 by terminal n'), (instances.TransitionType.REDUCE, 18)]])


class CalcLL1Lexer(lexer.Lexer):
    def __init__(self, inputStream: input_streams.InputStream):
        self._lexer = lexer.lexer(terminals, skipTerminals, inputStream)

    def next(self) -> instances.Token:
        return next(self._lexer)


class CalcLL1Parser:
    def __init__(self, calcLL1Lexer: CalcLL1Lexer):
        self._parser = parser.Parser(nterminals, nterminalConstructors, rules, ruleConstructorByNum, ruleAndPosByNum, table, calcLL1Lexer)
        self._parseCnt = 0

    def parse(self, tree: bool = False) -> instances.NterminalContext:
        if self._parseCnt != 0:
            raise parser.ParserException('parser object can parse only once')
        self._parseCnt += 1
        return self._parser.parse(tree)

