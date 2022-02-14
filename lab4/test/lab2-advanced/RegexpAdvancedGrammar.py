from alr import instances
from alr import lexer
from alr import parser
from alr import input_streams


nterminals = None  # for context classes


class _SContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[0])


class SContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[1])


class OrContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[2])
        self.d = None
        self.cnt = None


class AndContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[5])
        self.d = None
        self.cnt = None


class Or_Context(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[7])
        self.d = None
        self.cnt = None


class StContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[13])
        self.d = None
        self.cnt = None


class And_Context(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[15])
        self.d = None
        self.cnt = None


class CContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[21])
        self.d = None
        self.cnt = None


class St_Context(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[23])
        self.d = None
        self.cnt = None


class _Rule1Context:
    def __init__(self):
        self.S = []
        self._C3 = []
        self.Or = []
        self._F4 = []


class _Rule4Context:
    def __init__(self):
        self.Or = []
        self._C6 = []
        self.And = []
        self._C8 = []
        self.Or_ = []
        self._F9 = []


class _Rule8Context:
    def __init__(self):
        self.Or_ = []
        self._terminal0 = []
        self._C10 = []
        self.Or = []
        self._F11 = []


class _Rule13Context:
    def __init__(self):
        self.And = []
        self._C14 = []
        self.St = []
        self._C16 = []
        self.And_ = []
        self._F17 = []


class _Rule17Context:
    def __init__(self):
        self.And_ = []
        self._C18 = []
        self.And = []
        self._F19 = []


class _Rule22Context:
    def __init__(self):
        self.St = []
        self._C22 = []
        self.C = []
        self._C24 = []
        self.St_ = []
        self._F25 = []


class _Rule26Context:
    def __init__(self):
        self.St_ = []
        self._terminal1 = []
        self._C26 = []
        self._F27 = []


class _Rule31Context:
    def __init__(self):
        self.C = []
        self._terminal2 = []
        self._C29 = []
        self.Or = []
        self._terminal3 = []
        self._F30 = []


class _Rule11Context:
    def __init__(self):
        self.Or_ = []
        self._F12 = []


class _Rule20Context:
    def __init__(self):
        self.And_ = []
        self._F20 = []


class _Rule29Context:
    def __init__(self):
        self.St_ = []
        self._F28 = []


class _Rule34Context:
    def __init__(self):
        self.C = []
        self.char = []
        self._F31 = []


class _C3Context(instances.NterminalContext):
    def __init__(self, parent: OrContext, rctx: _Rule1Context):
        super().__init__(nterminals[3])
        parent.d = 1
        parent.cnt = 0


class _C6Context(instances.NterminalContext):
    def __init__(self, parent: AndContext, rctx: _Rule4Context):
        super().__init__(nterminals[6])
        parent.d = rctx.Or[0].d + 1
        parent.cnt = rctx.Or[0].cnt


class _C8Context(instances.NterminalContext):
    def __init__(self, parent: Or_Context, rctx: _Rule4Context):
        super().__init__(nterminals[8])
        parent.d = rctx.Or[0].d + 1
        parent.cnt = rctx.And[0].res


class _C10Context(instances.NterminalContext):
    def __init__(self, parent: OrContext, rctx: _Rule8Context):
        super().__init__(nterminals[10])
        parent.d = rctx.Or_[0].d + 1
        parent.cnt = rctx.Or_[0].cnt


class _C14Context(instances.NterminalContext):
    def __init__(self, parent: StContext, rctx: _Rule13Context):
        super().__init__(nterminals[14])
        parent.d = rctx.And[0].d + 1
        parent.cnt = rctx.And[0].cnt


class _C16Context(instances.NterminalContext):
    def __init__(self, parent: And_Context, rctx: _Rule13Context):
        super().__init__(nterminals[16])
        parent.d = rctx.And[0].d + 1
        parent.cnt = rctx.St[0].res


class _C18Context(instances.NterminalContext):
    def __init__(self, parent: AndContext, rctx: _Rule17Context):
        super().__init__(nterminals[18])
        parent.d = rctx.And_[0].d + 1
        parent.cnt = rctx.And_[0].cnt


class _C22Context(instances.NterminalContext):
    def __init__(self, parent: CContext, rctx: _Rule22Context):
        super().__init__(nterminals[22])
        parent.d = rctx.St[0].d + 1
        parent.cnt = rctx.St[0].cnt


class _C24Context(instances.NterminalContext):
    def __init__(self, parent: St_Context, rctx: _Rule22Context):
        super().__init__(nterminals[24])
        parent.d = rctx.St[0].d + 1
        parent.cnt = rctx.C[0].res


class _C26Context(instances.NterminalContext):
    def __init__(self, parent: St_Context, rctx: _Rule26Context):
        super().__init__(nterminals[26])
        parent.d = rctx.St_[0].d + 1
        parent.cnt = rctx.St_[0].cnt + 1


class _C29Context(instances.NterminalContext):
    def __init__(self, parent: OrContext, rctx: _Rule31Context):
        super().__init__(nterminals[29])
        parent.d = rctx.C[0].d + 1
        parent.cnt = rctx.C[0].cnt


class _F4Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule1Context):
        super().__init__(nterminals[4])
        rctx.S[0].d = 0; rctx.S[0].res = rctx.Or[0].res


class _F9Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule4Context):
        super().__init__(nterminals[9])
        rctx.Or[0].res = rctx.Or_[0].res


class _F11Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule8Context):
        super().__init__(nterminals[11])
        rctx.Or_[0].res = rctx.Or[0].res


class _F12Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule11Context):
        super().__init__(nterminals[12])
        rctx.Or_[0].res = rctx.Or_[0].cnt


class _F17Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule13Context):
        super().__init__(nterminals[17])
        rctx.And[0].res = rctx.And_[0].res


class _F19Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule17Context):
        super().__init__(nterminals[19])
        rctx.And_[0].res = rctx.And[0].res


class _F20Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule20Context):
        super().__init__(nterminals[20])
        rctx.And_[0].res = rctx.And_[0].cnt


class _F25Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule22Context):
        super().__init__(nterminals[25])
        rctx.St[0].res = rctx.St_[0].res


class _F27Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule26Context):
        super().__init__(nterminals[27])
        rctx.St_[0].res = rctx.St_[1].res


class _F28Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule29Context):
        super().__init__(nterminals[28])
        rctx.St_[0].res = rctx.St_[0].cnt


class _F30Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule31Context):
        super().__init__(nterminals[30])
        rctx.C[0].res = rctx.Or[0].res


class _F31Context(instances.NterminalContext):
    def __init__(self, rctx: _Rule34Context):
        super().__init__(nterminals[31])
        rctx.C[0].res = rctx.C[0].cnt


terminals = [instances.Terminal("_terminal0", 0, "\|"), instances.Terminal("_terminal1", 1, "\*"), instances.Terminal("_terminal2", 2, "\("), instances.Terminal("_terminal3", 3, "\)"), instances.Terminal("char", 4, "[a-z]")]

skipTerminals = [instances.Terminal("ws", 0, "[ \n\t\r]+")]

nterminals = [instances.Nterminal("_S", 0), instances.Nterminal("S", 1), instances.Nterminal("Or", 2), instances.ConstructorSymbol("_C3", 3), instances.FuncSymbol("_F4", 4), instances.Nterminal("And", 5), instances.ConstructorSymbol("_C6", 6), instances.Nterminal("Or_", 7), instances.ConstructorSymbol("_C8", 8), instances.FuncSymbol("_F9", 9), instances.ConstructorSymbol("_C10", 10), instances.FuncSymbol("_F11", 11), instances.FuncSymbol("_F12", 12), instances.Nterminal("St", 13), instances.ConstructorSymbol("_C14", 14), instances.Nterminal("And_", 15), instances.ConstructorSymbol("_C16", 16), instances.FuncSymbol("_F17", 17), instances.ConstructorSymbol("_C18", 18), instances.FuncSymbol("_F19", 19), instances.FuncSymbol("_F20", 20), instances.Nterminal("C", 21), instances.ConstructorSymbol("_C22", 22), instances.Nterminal("St_", 23), instances.ConstructorSymbol("_C24", 24), instances.FuncSymbol("_F25", 25), instances.ConstructorSymbol("_C26", 26), instances.FuncSymbol("_F27", 27), instances.FuncSymbol("_F28", 28), instances.ConstructorSymbol("_C29", 29), instances.FuncSymbol("_F30", 30), instances.FuncSymbol("_F31", 31)]

rules = [instances.Rule(0, nterminals[0], [nterminals[1]]), instances.Rule(1, nterminals[1], [nterminals[3], nterminals[2], nterminals[4]]), instances.Rule(2, nterminals[3], []), instances.Rule(3, nterminals[4], []), instances.Rule(4, nterminals[2], [nterminals[6], nterminals[5], nterminals[8], nterminals[7], nterminals[9]]), instances.Rule(5, nterminals[6], []), instances.Rule(6, nterminals[8], []), instances.Rule(7, nterminals[9], []), instances.Rule(8, nterminals[7], [terminals[0], nterminals[10], nterminals[2], nterminals[11]]), instances.Rule(9, nterminals[10], []), instances.Rule(10, nterminals[11], []), instances.Rule(11, nterminals[7], [nterminals[12]]), instances.Rule(12, nterminals[12], []), instances.Rule(13, nterminals[5], [nterminals[14], nterminals[13], nterminals[16], nterminals[15], nterminals[17]]), instances.Rule(14, nterminals[14], []), instances.Rule(15, nterminals[16], []), instances.Rule(16, nterminals[17], []), instances.Rule(17, nterminals[15], [nterminals[18], nterminals[5], nterminals[19]]), instances.Rule(18, nterminals[18], []), instances.Rule(19, nterminals[19], []), instances.Rule(20, nterminals[15], [nterminals[20]]), instances.Rule(21, nterminals[20], []), instances.Rule(22, nterminals[13], [nterminals[22], nterminals[21], nterminals[24], nterminals[23], nterminals[25]]), instances.Rule(23, nterminals[22], []), instances.Rule(24, nterminals[24], []), instances.Rule(25, nterminals[25], []), instances.Rule(26, nterminals[23], [terminals[1], nterminals[26], nterminals[23], nterminals[27]]), instances.Rule(27, nterminals[26], []), instances.Rule(28, nterminals[27], []), instances.Rule(29, nterminals[23], [nterminals[28]]), instances.Rule(30, nterminals[28], []), instances.Rule(31, nterminals[21], [terminals[2], nterminals[29], nterminals[2], terminals[3], nterminals[30]]), instances.Rule(32, nterminals[29], []), instances.Rule(33, nterminals[30], []), instances.Rule(34, nterminals[21], [terminals[4], nterminals[31]]), instances.Rule(35, nterminals[31], [])]

nterminals[0].rules = [rules[0]]
nterminals[1].rules = [rules[1]]
nterminals[2].rules = [rules[4]]
nterminals[3].rules = [rules[2]]
nterminals[4].rules = [rules[3]]
nterminals[5].rules = [rules[13]]
nterminals[6].rules = [rules[5]]
nterminals[7].rules = [rules[8], rules[11]]
nterminals[8].rules = [rules[6]]
nterminals[9].rules = [rules[7]]
nterminals[10].rules = [rules[9]]
nterminals[11].rules = [rules[10]]
nterminals[12].rules = [rules[12]]
nterminals[13].rules = [rules[22]]
nterminals[14].rules = [rules[14]]
nterminals[15].rules = [rules[17], rules[20]]
nterminals[16].rules = [rules[15]]
nterminals[17].rules = [rules[16]]
nterminals[18].rules = [rules[18]]
nterminals[19].rules = [rules[19]]
nterminals[20].rules = [rules[21]]
nterminals[21].rules = [rules[31], rules[34]]
nterminals[22].rules = [rules[23]]
nterminals[23].rules = [rules[26], rules[29]]
nterminals[24].rules = [rules[24]]
nterminals[25].rules = [rules[25]]
nterminals[26].rules = [rules[27]]
nterminals[27].rules = [rules[28]]
nterminals[28].rules = [rules[30]]
nterminals[29].rules = [rules[32]]
nterminals[30].rules = [rules[33]]
nterminals[31].rules = [rules[35]]

nterminalConstructors = [_SContext, SContext, OrContext, _C3Context, _F4Context, AndContext, _C6Context, Or_Context, _C8Context, _F9Context, _C10Context, _F11Context, _F12Context, StContext, _C14Context, And_Context, _C16Context, _F17Context, _C18Context, _F19Context, _F20Context, CContext, _C22Context, St_Context, _C24Context, _F25Context, _C26Context, _F27Context, _F28Context, _C29Context, _F30Context, _F31Context]

ruleConstructorByNum = {1: _Rule1Context, 4: _Rule4Context, 8: _Rule8Context, 13: _Rule13Context, 17: _Rule17Context, 22: _Rule22Context, 26: _Rule26Context, 31: _Rule31Context, 11: _Rule11Context, 20: _Rule20Context, 29: _Rule29Context, 34: _Rule34Context}

ruleAndPosByNum = {3: (1, 0), 4: (1, 2), 6: (4, 0), 8: (4, 2), 9: (4, 4), 10: (8, 1), 11: (8, 3), 12: (11, 0), 14: (13, 0), 16: (13, 2), 17: (13, 4), 18: (17, 0), 19: (17, 2), 20: (20, 0), 22: (22, 0), 24: (22, 2), 25: (22, 4), 26: (26, 1), 27: (26, 3), 28: (29, 0), 29: (31, 1), 30: (31, 4), 31: (34, 1)}

table = instances.Table([[instances.TransitionType.BAD, 1, instances.TransitionType.BAD, 2, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, 3, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 4, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 5, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 6, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 7, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 8, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 9, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 10, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 11, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 12, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 14, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 15, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 18, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 19, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 20, instances.TransitionType.BAD, instances.TransitionType.BAD, 21, instances.TransitionType.BAD, 22, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 23, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 24, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 25], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, 26, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 4, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 27, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 28, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 7, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 29, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 30, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, 32, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 4, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 33, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 34, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 35, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 36, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 38, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 30, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 39, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 40, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD]], [[(instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal1'), (instances.TransitionType.REDUCE, 2), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal3'), (instances.TransitionType.REDUCE, 2), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _END')], [(instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal char'), (instances.TransitionType.REDUCE, 0)], [(instances.TransitionType.BAD, 'no transition from state 2 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 2 by terminal _terminal1'), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.BAD, 'no transition from state 2 by terminal _terminal3'), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.BAD, 'no transition from state 2 by terminal _END')], [(instances.TransitionType.BAD, 'no transition from state 3 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 3 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 3 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 3 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 3 by terminal char'), (instances.TransitionType.REDUCE, 3)], [(instances.TransitionType.BAD, 'no transition from state 4 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 4 by terminal _terminal1'), (instances.TransitionType.REDUCE, 14), (instances.TransitionType.BAD, 'no transition from state 4 by terminal _terminal3'), (instances.TransitionType.REDUCE, 14), (instances.TransitionType.BAD, 'no transition from state 4 by terminal _END')], [(instances.TransitionType.BAD, 'no transition from state 5 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 5 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 5 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 5 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 5 by terminal char'), (instances.TransitionType.REDUCE, 1)], [(instances.TransitionType.REDUCE, 6), (instances.TransitionType.BAD, 'no transition from state 6 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 6 by terminal _terminal2'), (instances.TransitionType.REDUCE, 6), (instances.TransitionType.BAD, 'no transition from state 6 by terminal char'), (instances.TransitionType.REDUCE, 6)], [(instances.TransitionType.BAD, 'no transition from state 7 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 7 by terminal _terminal1'), (instances.TransitionType.REDUCE, 23), (instances.TransitionType.BAD, 'no transition from state 7 by terminal _terminal3'), (instances.TransitionType.REDUCE, 23), (instances.TransitionType.BAD, 'no transition from state 7 by terminal _END')], [(instances.TransitionType.SHIFT, 13), (instances.TransitionType.BAD, 'no transition from state 8 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 8 by terminal _terminal2'), (instances.TransitionType.REDUCE, 12), (instances.TransitionType.BAD, 'no transition from state 8 by terminal char'), (instances.TransitionType.REDUCE, 12)], [(instances.TransitionType.REDUCE, 15), (instances.TransitionType.BAD, 'no transition from state 9 by terminal _terminal1'), (instances.TransitionType.REDUCE, 15), (instances.TransitionType.REDUCE, 15), (instances.TransitionType.REDUCE, 15), (instances.TransitionType.REDUCE, 15)], [(instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal1'), (instances.TransitionType.SHIFT, 16), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal3'), (instances.TransitionType.SHIFT, 17), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _END')], [(instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal2'), (instances.TransitionType.REDUCE, 7), (instances.TransitionType.BAD, 'no transition from state 11 by terminal char'), (instances.TransitionType.REDUCE, 7)], [(instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 12 by terminal _terminal2'), (instances.TransitionType.REDUCE, 11), (instances.TransitionType.BAD, 'no transition from state 12 by terminal char'), (instances.TransitionType.REDUCE, 11)], [(instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal1'), (instances.TransitionType.REDUCE, 9), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _terminal3'), (instances.TransitionType.REDUCE, 9), (instances.TransitionType.BAD, 'no transition from state 13 by terminal _END')], [(instances.TransitionType.REDUCE, 21), (instances.TransitionType.BAD, 'no transition from state 14 by terminal _terminal1'), (instances.TransitionType.REDUCE, 18), (instances.TransitionType.REDUCE, 21), (instances.TransitionType.REDUCE, 18), (instances.TransitionType.REDUCE, 21)], [(instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24), (instances.TransitionType.REDUCE, 24)], [(instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal1'), (instances.TransitionType.REDUCE, 32), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _terminal3'), (instances.TransitionType.REDUCE, 32), (instances.TransitionType.BAD, 'no transition from state 16 by terminal _END')], [(instances.TransitionType.REDUCE, 35), (instances.TransitionType.REDUCE, 35), (instances.TransitionType.REDUCE, 35), (instances.TransitionType.REDUCE, 35), (instances.TransitionType.REDUCE, 35), (instances.TransitionType.REDUCE, 35)], [(instances.TransitionType.BAD, 'no transition from state 18 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 18 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 18 by terminal _terminal2'), (instances.TransitionType.REDUCE, 4), (instances.TransitionType.BAD, 'no transition from state 18 by terminal char'), (instances.TransitionType.REDUCE, 4)], [(instances.TransitionType.BAD, 'no transition from state 19 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 19 by terminal _terminal1'), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.BAD, 'no transition from state 19 by terminal _terminal3'), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.BAD, 'no transition from state 19 by terminal _END')], [(instances.TransitionType.REDUCE, 16), (instances.TransitionType.BAD, 'no transition from state 20 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 20 by terminal _terminal2'), (instances.TransitionType.REDUCE, 16), (instances.TransitionType.BAD, 'no transition from state 20 by terminal char'), (instances.TransitionType.REDUCE, 16)], [(instances.TransitionType.BAD, 'no transition from state 21 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 21 by terminal _terminal1'), (instances.TransitionType.REDUCE, 14), (instances.TransitionType.BAD, 'no transition from state 21 by terminal _terminal3'), (instances.TransitionType.REDUCE, 14), (instances.TransitionType.BAD, 'no transition from state 21 by terminal _END')], [(instances.TransitionType.REDUCE, 20), (instances.TransitionType.BAD, 'no transition from state 22 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 22 by terminal _terminal2'), (instances.TransitionType.REDUCE, 20), (instances.TransitionType.BAD, 'no transition from state 22 by terminal char'), (instances.TransitionType.REDUCE, 20)], [(instances.TransitionType.REDUCE, 30), (instances.TransitionType.SHIFT, 31), (instances.TransitionType.REDUCE, 30), (instances.TransitionType.REDUCE, 30), (instances.TransitionType.REDUCE, 30), (instances.TransitionType.REDUCE, 30)], [(instances.TransitionType.BAD, 'no transition from state 24 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 24 by terminal _terminal1'), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.BAD, 'no transition from state 24 by terminal _terminal3'), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.BAD, 'no transition from state 24 by terminal _END')], [(instances.TransitionType.REDUCE, 34), (instances.TransitionType.REDUCE, 34), (instances.TransitionType.REDUCE, 34), (instances.TransitionType.REDUCE, 34), (instances.TransitionType.REDUCE, 34), (instances.TransitionType.REDUCE, 34)], [(instances.TransitionType.BAD, 'no transition from state 26 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 26 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 26 by terminal _terminal2'), (instances.TransitionType.REDUCE, 10), (instances.TransitionType.BAD, 'no transition from state 26 by terminal char'), (instances.TransitionType.REDUCE, 10)], [(instances.TransitionType.REDUCE, 13), (instances.TransitionType.BAD, 'no transition from state 27 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 27 by terminal _terminal2'), (instances.TransitionType.REDUCE, 13), (instances.TransitionType.BAD, 'no transition from state 27 by terminal char'), (instances.TransitionType.REDUCE, 13)], [(instances.TransitionType.REDUCE, 19), (instances.TransitionType.BAD, 'no transition from state 28 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 28 by terminal _terminal2'), (instances.TransitionType.REDUCE, 19), (instances.TransitionType.BAD, 'no transition from state 28 by terminal char'), (instances.TransitionType.REDUCE, 19)], [(instances.TransitionType.REDUCE, 25), (instances.TransitionType.BAD, 'no transition from state 29 by terminal _terminal1'), (instances.TransitionType.REDUCE, 25), (instances.TransitionType.REDUCE, 25), (instances.TransitionType.REDUCE, 25), (instances.TransitionType.REDUCE, 25)], [(instances.TransitionType.REDUCE, 29), (instances.TransitionType.BAD, 'no transition from state 30 by terminal _terminal1'), (instances.TransitionType.REDUCE, 29), (instances.TransitionType.REDUCE, 29), (instances.TransitionType.REDUCE, 29), (instances.TransitionType.REDUCE, 29)], [(instances.TransitionType.REDUCE, 27), (instances.TransitionType.REDUCE, 27), (instances.TransitionType.REDUCE, 27), (instances.TransitionType.REDUCE, 27), (instances.TransitionType.REDUCE, 27), (instances.TransitionType.REDUCE, 27)], [(instances.TransitionType.BAD, 'no transition from state 32 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 32 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 32 by terminal _terminal2'), (instances.TransitionType.SHIFT, 37), (instances.TransitionType.BAD, 'no transition from state 32 by terminal char'), (instances.TransitionType.BAD, 'no transition from state 32 by terminal _END')], [(instances.TransitionType.BAD, 'no transition from state 33 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 33 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 33 by terminal _terminal2'), (instances.TransitionType.REDUCE, 8), (instances.TransitionType.BAD, 'no transition from state 33 by terminal char'), (instances.TransitionType.REDUCE, 8)], [(instances.TransitionType.REDUCE, 17), (instances.TransitionType.BAD, 'no transition from state 34 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 34 by terminal _terminal2'), (instances.TransitionType.REDUCE, 17), (instances.TransitionType.BAD, 'no transition from state 34 by terminal char'), (instances.TransitionType.REDUCE, 17)], [(instances.TransitionType.REDUCE, 22), (instances.TransitionType.BAD, 'no transition from state 35 by terminal _terminal1'), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.REDUCE, 22), (instances.TransitionType.REDUCE, 22)], [(instances.TransitionType.REDUCE, 30), (instances.TransitionType.SHIFT, 31), (instances.TransitionType.REDUCE, 30), (instances.TransitionType.REDUCE, 30), (instances.TransitionType.REDUCE, 30), (instances.TransitionType.REDUCE, 30)], [(instances.TransitionType.REDUCE, 33), (instances.TransitionType.REDUCE, 33), (instances.TransitionType.REDUCE, 33), (instances.TransitionType.REDUCE, 33), (instances.TransitionType.REDUCE, 33), (instances.TransitionType.REDUCE, 33)], [(instances.TransitionType.REDUCE, 28), (instances.TransitionType.BAD, 'no transition from state 38 by terminal _terminal1'), (instances.TransitionType.REDUCE, 28), (instances.TransitionType.REDUCE, 28), (instances.TransitionType.REDUCE, 28), (instances.TransitionType.REDUCE, 28)], [(instances.TransitionType.REDUCE, 31), (instances.TransitionType.REDUCE, 31), (instances.TransitionType.REDUCE, 31), (instances.TransitionType.REDUCE, 31), (instances.TransitionType.REDUCE, 31), (instances.TransitionType.REDUCE, 31)], [(instances.TransitionType.REDUCE, 26), (instances.TransitionType.BAD, 'no transition from state 40 by terminal _terminal1'), (instances.TransitionType.REDUCE, 26), (instances.TransitionType.REDUCE, 26), (instances.TransitionType.REDUCE, 26), (instances.TransitionType.REDUCE, 26)]])


class RegexpAdvancedLexer(lexer.Lexer):
    def __init__(self, inputStream: input_streams.InputStream):
        self._lexer = lexer.lexer(terminals, skipTerminals, inputStream)

    def next(self) -> instances.Token:
        return next(self._lexer)


class RegexpAdvancedParser:
    def __init__(self, regexpAdvancedLexer: RegexpAdvancedLexer):
        self._parser = parser.Parser(nterminals, nterminalConstructors, rules, ruleConstructorByNum, ruleAndPosByNum, table, regexpAdvancedLexer)
        self._parseCnt = 0

    def parse(self, tree: bool = False) -> instances.NterminalContext:
        if self._parseCnt != 0:
            raise parser.ParserException('parser object can parse only once')
        self._parseCnt += 1
        return self._parser.parse(tree)

