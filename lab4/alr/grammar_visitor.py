from typing import Any, Optional, Callable, Tuple, List

from alr.antlr.ALRParser import ALRParser
from alr.antlr.ALRVisitor import ALRVisitor
from alr.instances import Terminal, Nterminal, Rule, ConstructorSymbol, FuncSymbol, INIT_NTERMINAL_NAME


class GrammarException(Exception):
    pass


def splitConstructor(constructor: str) -> [str]:
    return [arg.strip() for arg in constructor[1:-1].split(',')]


def checkConstructorDef(nterminalName: str, attrs: [str]):
    for attr in attrs:
        if not attr[0].isalpha():
            raise GrammarException(f'Attr {attr} of nterminal {nterminalName} starts not with a character')
        for c in attr[1:]:
            if not (c.isalpha() or c.isdigit() or c == '_'):
                raise GrammarException(f'Attr {attr} of nterminal {nterminalName} must contain only characters, '
                                       f'digits and _, but was found {c} ')


def cnt(lst: [Any]) -> int:
    return 0 if lst is None else len(lst)


def checkConstructorAttrs(attrs: [str], nterminalName: str):
    if len(attrs) == 1 and len(attrs[0]) == 0:
        raise GrammarException(f'nterminal {nterminalName} has constructor call with 0 args')


class GrammarVisitor(ALRVisitor):
    def __init__(self, start):
        self.start = start

        self.nterminals = []
        self.nterminalByName = {}
        self.nterminalCntAttrs = []  # number of attributes

        self.rules = []

        self.terminals = []
        self.terminalByName = {}

        self.skipTerminalByName = {}

        self.constructorDefByNum = {}  # get constructor definition by nterminal number
        self.constructorCallByNum = {}  # get constructor call by translation symbol number
        self.funcByNum = {}  # get func body by translation symbol number

        self.ruleAndPosByNum = {}

        initNterminal = self.addNterminal(INIT_NTERMINAL_NAME)
        rule = self.addRule(initNterminal)
        startNterminal = self.addNterminal(start)
        rule.right.append(startNterminal)

    # Terminals

    def getTerminal(self, terminalName: str) -> Terminal:
        if self.hasTerminal(terminalName):
            return self.terminalByName[terminalName]
        else:
            return self.addTerminal(terminalName)

    def hasTerminal(self, terminalName: str) -> bool:
        return terminalName in self.terminalByName

    def addTerminal(self, terminalName: str, regexp: Optional[str] = None) -> Terminal:
        num = len(self.terminals)
        terminal = Terminal(terminalName, num, regexp)
        self.terminalByName[terminalName] = terminal
        self.terminals.append(terminal)
        return terminal

    # Nterminals

    def getNterminal(self, nterminalName: str) -> Nterminal:
        if self.hasNterminal(nterminalName):
            return self.nterminalByName[nterminalName]
        else:
            return self.addNterminal(nterminalName)

    def hasNterminal(self, nterminalName: str) -> bool:
        return nterminalName in self.nterminalByName

    def addNterminal(self, nterminalName: str, cntAttrs: int = 0,
                     constructor: Callable[[str, int], Nterminal] = Nterminal) -> Nterminal:
        num = len(self.nterminals)
        nterminal = constructor(nterminalName, num)
        self.nterminalByName[nterminalName] = nterminal
        self.nterminals.append(nterminal)
        self.nterminalCntAttrs.append(cntAttrs)
        return nterminal

    # Helpful methods

    def addRule(self, nterminal: Nterminal) -> Rule:
        rule = Rule(len(self.rules), nterminal, [])
        nterminal.rules.append(rule)
        self.rules.append(rule)
        return rule

    def addConstructorCall(self, ruleNum: int, constructorCallPos: int, nterminal: Nterminal,
                           constructorCallArgs: [str]) -> ConstructorSymbol:
        cntArgs = len(constructorCallArgs)
        if cntArgs == 0:
            raise GrammarException(f'Can not call {nterminal.name} with zero arg constructor')

        self.checkCntAttrs(cntArgs, nterminal)

        constructorCallName = f'_C{len(self.nterminals)}'
        constructorCall = self.addNterminal(constructorCallName, constructor=ConstructorSymbol)

        self.addRule(constructorCall)
        self.constructorCallByNum[constructorCall.num] = constructorCallArgs
        self.ruleAndPosByNum[constructorCall.num] = (ruleNum, constructorCallPos)

        return constructorCall

    def checkCntAttrs(self, cntAttrs: int, nterminal: Nterminal):
        cnt_expected = self.nterminalCntAttrs[nterminal.num]
        if cnt_expected != cntAttrs:
            raise GrammarException(f"Nterminal {nterminal.name} expects to have constructor with {cnt_expected} args, "
                                   f"but found with {cntAttrs}")

    def addFunc(self, ruleNum: int, funcPos: int, funcBody: str) -> FuncSymbol:
        funcName = f'_F{len(self.nterminals)}'
        func = self.addNterminal(funcName, constructor=FuncSymbol)

        self.addRule(func)
        self.funcByNum[func.num] = funcBody[1:-1].strip()
        self.ruleAndPosByNum[func.num] = (ruleNum, funcPos)

        return func

    def processRuleStart(self, nterminalName: str, attrs: [str]) -> Nterminal:
        cntAttrs = cnt(attrs)
        if self.hasNterminal(nterminalName):
            nterminal = self.nterminalByName[nterminalName]
            self.checkCntAttrs(cntAttrs, nterminal)
            num = nterminal.num
            if num in self.constructorDefByNum:
                if attrs != self.constructorDefByNum[num]:
                    raise GrammarException(f'nterminal {nterminalName} has constructors with different attrs')
            elif attrs is not None:
                self.addConstructorDef(attrs, nterminal)
        else:
            nterminal = self.addNterminal(nterminalName, cntAttrs)
            if attrs is not None:
                self.addConstructorDef(attrs, nterminal)
        return nterminal

    def addConstructorDef(self, attrs: [str], nterminal: Nterminal):
        checkConstructorAttrs(attrs, nterminal.name)
        checkConstructorDef(nterminal.name, attrs)
        self.constructorDefByNum[nterminal.num] = attrs

    def visitStart(self, ctx: ALRParser.StartContext):
        for ctx in ctx.desc():
            self.visit(ctx)
        if self.start not in self.nterminalByName:  # в переданной грамматике должен быть стартовый нетерминал
            raise GrammarException(f"Haven't found start nterminal {self.start} in grammar")
        for terminal in self.terminals:  # проверка, что у каждого терминала есть regexp
            if terminal.regexp is None:
                raise GrammarException(f"Haven't found regexp for terminal {terminal.name}")
        for nterminal in self.nterminals:  # Для каждого нетерминала по крайней мере есть одно правилоа
            if not nterminal.rules:
                raise GrammarException(f"Nterminal {nterminal.name} has no rules")

    def visitDescRule(self, ctx: ALRParser.DescRuleContext):
        nterminal_name, attrs = self.visit(ctx.nterminal())
        ruleStartNterminal = self.processRuleStart(nterminal_name, attrs)
        for right in ctx.rights().right():
            rule = self.addRule(ruleStartNterminal)
            if isinstance(right, ALRParser.RightEpsContext):
                continue
            shift = 0
            for pos, member in enumerate(right.member()):
                if isinstance(member, ALRParser.MemberTerminalContext):
                    self.addTerminalToRule(member, rule)
                elif isinstance(member, ALRParser.MemberRegexpContext):
                    self.addRegexpToRule(member, rule)
                elif isinstance(member, ALRParser.MemberNterminalContext):
                    shift += self.addNterminalToRule(member, pos + shift, rule)
                elif isinstance(member, ALRParser.MemberFuncContext):
                    self.addFuncToRule(member, pos + shift, rule)

    def addTerminalToRule(self, member: ALRParser.MemberTerminalContext, rule: Rule):
        terminalName = member.terminal().TERMINAL().getText()
        terminal = self.getTerminal(terminalName)
        rule.right.append(terminal)

    def addRegexpToRule(self, member: ALRParser.MemberRegexpContext, rule: Rule):
        terminalName = f"_terminal{len(self.terminals)}"
        terminal = self.addTerminal(terminalName, member.regexp().REGEXP().getText()[1:-1])
        rule.right.append(terminal)

    def addNterminalToRule(self, member: ALRParser.MemberNterminalContext, pos: int, rule: Rule) -> int:
        nterminalName, attrs = self.visit(member.nterminal())
        if not self.hasNterminal(nterminalName):
            nterminal = self.addNterminal(nterminalName, cnt(attrs))
        else:
            nterminal = self.getNterminal(nterminalName)

        self.checkCntAttrs(cnt(attrs), nterminal)

        toReturn = 0
        if attrs is not None:
            checkConstructorAttrs(attrs, nterminalName)
            constructor_call = self.addConstructorCall(ruleNum=rule.num, constructorCallPos=pos,
                                                       nterminal=nterminal, constructorCallArgs=attrs)
            rule.right.append(constructor_call)
            toReturn = 1
        rule.right.append(nterminal)
        return toReturn

    def addFuncToRule(self, member: ALRParser.MemberFuncContext, pos: int, rule: Rule):
        func_body = member.func().FUNC().getText()
        func_call = self.addFunc(ruleNum=rule.num, funcPos=pos, funcBody=func_body)
        rule.right.append(func_call)

    def visitDescTerminal(self, ctx: ALRParser.DescTerminalContext) -> Terminal:
        terminalName = ctx.terminal().TERMINAL().getText()
        regexp = ctx.regexp().REGEXP().getText()[1:-1]
        terminal = self.getTerminal(terminalName)
        if terminal.regexp is not None:
            raise GrammarException(f"Redefinition of terminal {terminalName}")
        terminal.regexp = regexp
        return terminal

    def visitDescSkip(self, ctx: ALRParser.DescSkipContext):
        terminalName = ctx.terminal().TERMINAL().getText()
        regexp = ctx.regexp().REGEXP().getText()[1:-1]
        if terminalName in self.skipTerminalByName:
            raise GrammarException(f'Redefinition of skip terminal {terminalName}')
        self.skipTerminalByName[terminalName] = Terminal(terminalName, len(self.skipTerminalByName), regexp)

    def visitNterminal(self, ctx: ALRParser.NterminalContext) -> Tuple[str, List[str]]:
        constructor = ctx.CONSTRUCTOR()
        attrs = splitConstructor(constructor.getText()) if constructor else None
        return ctx.NTERMINAL().getText(), attrs
