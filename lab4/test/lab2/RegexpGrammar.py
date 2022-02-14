from alr import instances
from alr import lexer
from alr import parser
from alr import input_streams


nterminals = None  # for context classes


class _SContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[0])


class OrContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[1])


class AndContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[2])


class StContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[3])


class CContext(instances.NterminalContext):
    def __init__(self):
        super().__init__(nterminals[4])


terminals = [instances.Terminal("_terminal0", 0, "\|"), instances.Terminal("_terminal1", 1, "\*"), instances.Terminal("_terminal2", 2, "\("), instances.Terminal("_terminal3", 3, "\)"), instances.Terminal("char", 4, "[a-z]")]

skipTerminals = [instances.Terminal("ws", 0, "[ \n\t\r]+")]

nterminals = [instances.Nterminal("_S", 0), instances.Nterminal("Or", 1), instances.Nterminal("And", 2), instances.Nterminal("St", 3), instances.Nterminal("C", 4)]

rules = [instances.Rule(0, nterminals[0], [nterminals[1]]), instances.Rule(1, nterminals[1], [nterminals[1], terminals[0], nterminals[2]]), instances.Rule(2, nterminals[1], [nterminals[2]]), instances.Rule(3, nterminals[2], [nterminals[2], nterminals[3]]), instances.Rule(4, nterminals[2], [nterminals[3]]), instances.Rule(5, nterminals[3], [nterminals[3], terminals[1]]), instances.Rule(6, nterminals[3], [nterminals[4]]), instances.Rule(7, nterminals[4], [terminals[2], nterminals[1], terminals[3]]), instances.Rule(8, nterminals[4], [terminals[4]])]

nterminals[0].rules = [rules[0]]
nterminals[1].rules = [rules[1], rules[2]]
nterminals[2].rules = [rules[3], rules[4]]
nterminals[3].rules = [rules[5], rules[6]]
nterminals[4].rules = [rules[7], rules[8]]

nterminalConstructors = [_SContext, OrContext, AndContext, StContext, CContext]

ruleConstructorByNum = {}

ruleAndPosByNum = {}

table = instances.Table([[instances.TransitionType.BAD, 1, 2, 3, 4], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 8, 4], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, 10, 2, 3, 4], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, 11, 3, 4], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, 8, 4], [instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD, instances.TransitionType.BAD]], [[(instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal1'), (instances.TransitionType.SHIFT, 5), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _terminal3'), (instances.TransitionType.SHIFT, 6), (instances.TransitionType.BAD, 'no transition from state 0 by terminal _END')], [(instances.TransitionType.SHIFT, 7), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal2'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal _terminal3'), (instances.TransitionType.BAD, 'no transition from state 1 by terminal char'), (instances.TransitionType.REDUCE, 0)], [(instances.TransitionType.REDUCE, 2), (instances.TransitionType.BAD, 'no transition from state 2 by terminal _terminal1'), (instances.TransitionType.SHIFT, 5), (instances.TransitionType.REDUCE, 2), (instances.TransitionType.SHIFT, 6), (instances.TransitionType.REDUCE, 2)], [(instances.TransitionType.REDUCE, 4), (instances.TransitionType.SHIFT, 9), (instances.TransitionType.REDUCE, 4), (instances.TransitionType.REDUCE, 4), (instances.TransitionType.REDUCE, 4), (instances.TransitionType.REDUCE, 4)], [(instances.TransitionType.REDUCE, 6), (instances.TransitionType.REDUCE, 6), (instances.TransitionType.REDUCE, 6), (instances.TransitionType.REDUCE, 6), (instances.TransitionType.REDUCE, 6), (instances.TransitionType.REDUCE, 6)], [(instances.TransitionType.BAD, 'no transition from state 5 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 5 by terminal _terminal1'), (instances.TransitionType.SHIFT, 5), (instances.TransitionType.BAD, 'no transition from state 5 by terminal _terminal3'), (instances.TransitionType.SHIFT, 6), (instances.TransitionType.BAD, 'no transition from state 5 by terminal _END')], [(instances.TransitionType.REDUCE, 8), (instances.TransitionType.REDUCE, 8), (instances.TransitionType.REDUCE, 8), (instances.TransitionType.REDUCE, 8), (instances.TransitionType.REDUCE, 8), (instances.TransitionType.REDUCE, 8)], [(instances.TransitionType.BAD, 'no transition from state 7 by terminal _terminal0'), (instances.TransitionType.BAD, 'no transition from state 7 by terminal _terminal1'), (instances.TransitionType.SHIFT, 5), (instances.TransitionType.BAD, 'no transition from state 7 by terminal _terminal3'), (instances.TransitionType.SHIFT, 6), (instances.TransitionType.BAD, 'no transition from state 7 by terminal _END')], [(instances.TransitionType.REDUCE, 3), (instances.TransitionType.SHIFT, 9), (instances.TransitionType.REDUCE, 3), (instances.TransitionType.REDUCE, 3), (instances.TransitionType.REDUCE, 3), (instances.TransitionType.REDUCE, 3)], [(instances.TransitionType.REDUCE, 5), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.REDUCE, 5), (instances.TransitionType.REDUCE, 5)], [(instances.TransitionType.SHIFT, 7), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal1'), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _terminal2'), (instances.TransitionType.SHIFT, 12), (instances.TransitionType.BAD, 'no transition from state 10 by terminal char'), (instances.TransitionType.BAD, 'no transition from state 10 by terminal _END')], [(instances.TransitionType.REDUCE, 1), (instances.TransitionType.BAD, 'no transition from state 11 by terminal _terminal1'), (instances.TransitionType.SHIFT, 5), (instances.TransitionType.REDUCE, 1), (instances.TransitionType.SHIFT, 6), (instances.TransitionType.REDUCE, 1)], [(instances.TransitionType.REDUCE, 7), (instances.TransitionType.REDUCE, 7), (instances.TransitionType.REDUCE, 7), (instances.TransitionType.REDUCE, 7), (instances.TransitionType.REDUCE, 7), (instances.TransitionType.REDUCE, 7)]])


class RegexpLexer(lexer.Lexer):
    def __init__(self, inputStream: input_streams.InputStream):
        self._lexer = lexer.lexer(terminals, skipTerminals, inputStream)

    def next(self) -> instances.Token:
        return next(self._lexer)


class RegexpParser:
    def __init__(self, regexpLexer: RegexpLexer):
        self._parser = parser.Parser(nterminals, nterminalConstructors, rules, ruleConstructorByNum, ruleAndPosByNum, table, regexpLexer)
        self._parseCnt = 0

    def parse(self, tree: bool = False) -> instances.NterminalContext:
        if self._parseCnt != 0:
            raise parser.ParserException('parser object can parse only once')
        self._parseCnt += 1
        return self._parser.parse(tree)

