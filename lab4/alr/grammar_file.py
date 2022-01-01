import re
from typing import Optional, List, TextIO

from alr.grammar_visitor import GrammarVisitor
from alr.instances import Table, TranslationSymbol, Nterminal
from alr.utils import getPythonFileName, writeLine, writeLine2, writeLine3

_instancesPackage = "instances"


class MethodInfo:
    def __init__(self, name: str, args: Optional[List[str]] = None, returnType: Optional[str] = None,
                 body: Optional[List[str]] = None):
        self.name = name
        self.args = args
        self.returnType = returnType
        self.body = body

    def write(self, rf: TextIO, initialIndent: int = 0):
        args = ', '.join(self.args) if self.args else ''
        returnType = f' -> {self.returnType}' if self.returnType else ''
        writeLine(rf, f"def {self.name}({args}){returnType}:", initialIndent)
        if self.body:
            for line in self.body:
                writeLine(rf, line, initialIndent + 1)


class ClassInfo:
    def __init__(self, className: str, parent: Optional[str] = None, methods: Optional[List[MethodInfo]] = None):
        self.className = className
        self.parent = parent
        self.methods = methods

    def write(self, rf: TextIO):
        parent = f'({self.parent})' if self.parent else ''
        writeLine(rf, f"class {self.className}{parent}:")

        if self.methods:
            for method in self.methods:
                method.write(rf, 1)
                writeLine(rf)


def transformCode(code: str) -> str:
    code = re.sub(r'#([\w\d_]+)\.', r'#\1[0].', code)  # #E.val -> #E[0].val
    code = re.sub(r'#([\w\d_\[\]]+)\.', r'rctx.\1.', code)  # #E[i].val -> rctx.E[i].val
    return code


def generateRuleContextClassName(ruleNum):
    return f"_Rule{ruleNum}Context"


def generateInitMethodInfo(args: Optional[List[str]] = None, body: Optional[List[str]] = None):
    return MethodInfo("__init__", args=["self", *(args if args else [])], body=body)


def generateRuleClass(ruleNum: int, visitor: GrammarVisitor) -> ClassInfo:
    rule = visitor.rules[ruleNum]
    was = {rule.left.name}
    initBody = [f"self.{rule.left.name} = []"]
    for kind in rule.right:
        if kind.name not in was:
            initBody.append(f"self.{kind.name} = []")
            was.add(kind.name)
    className = generateRuleContextClassName(ruleNum)
    return ClassInfo(className=className, parent=None, methods=[generateInitMethodInfo(body=initBody)])


def generateSuperCallForNterminal(nterminal: Nterminal) -> str:
    return f"super().__init__(nterminals[{nterminal.num}])"


def generateConstructorClasses(visitor: GrammarVisitor, generatedRuleByRuleNum: dict[int, ClassInfo]) -> [ClassInfo]:
    constructorClasses = []
    parent = f"{_instancesPackage}.NterminalContext"

    for constructorNum, constructorArgs in visitor.constructorCallByNum.items():
        parentRuleNum, index = visitor.ruleAndPosByNum[constructorNum]
        if parentRuleNum not in generatedRuleByRuleNum:
            generatedRuleByRuleNum[parentRuleNum] = generateRuleClass(parentRuleNum, visitor)

        constructorNterminal = visitor.nterminals[constructorNum]
        nterminal = visitor.rules[parentRuleNum].right[index + 1]

        className = f'{constructorNterminal.name}Context'

        initBody = [generateSuperCallForNterminal(constructorNterminal)]
        for attr_name, attr_val in zip(visitor.constructorDefByNum[nterminal.num], constructorArgs):
            initBody.append(f"parent.{attr_name} = {transformCode(attr_val)}")

        initArgs = [f"parent: {nterminal.name}Context", f"rctx: {generateRuleContextClassName(parentRuleNum)}"]

        constructorClasses.append(ClassInfo(className, parent, [generateInitMethodInfo(initArgs, initBody)]))
    return constructorClasses


def generateFuncClasses(visitor: GrammarVisitor, generatedRuleByRuleNum: dict[int, ClassInfo]) -> [ClassInfo]:
    funcClasses = []
    parent = f"{_instancesPackage}.NterminalContext"

    for funcNum, funcBody in visitor.funcByNum.items():
        parentRuleNum, _ = visitor.ruleAndPosByNum[funcNum]
        if parentRuleNum not in generatedRuleByRuleNum:
            generatedRuleByRuleNum[parentRuleNum] = generateRuleClass(parentRuleNum, visitor)

        funcNterminal = visitor.nterminals[funcNum]

        className = f'{funcNterminal.name}Context'
        initBody = [generateSuperCallForNterminal(funcNterminal)]
        for code_line in funcBody.split('\n'):
            initBody.append(transformCode(code_line))

        initArgs = [f"rctx: {generateRuleContextClassName(parentRuleNum)}"]

        funcClasses.append(ClassInfo(className, parent, [generateInitMethodInfo(initArgs, initBody)]))
    return funcClasses


def generateNterminalClasses(visitor: GrammarVisitor) -> [ClassInfo]:
    nterminalClasses = []
    parent = f"{_instancesPackage}.NterminalContext"
    for nterminal in visitor.nterminals:
        if isinstance(nterminal, TranslationSymbol):
            continue

        initBody = [generateSuperCallForNterminal(nterminal)]

        if nterminal.num in visitor.constructorDefByNum:
            for attr in visitor.constructorDefByNum[nterminal.num]:
                initBody.append(f"self.{attr} = None")

        className = f'{nterminal.name}Context'
        methods = [generateInitMethodInfo(body=initBody)]

        nterminalClasses.append(ClassInfo(className, parent, methods))
    return nterminalClasses


def writeImports(rf: TextIO):
    writeLine(rf, "from alr import instances")
    writeLine(rf, "from alr import lexer")
    writeLine(rf, "from alr import parser")
    writeLine(rf, "from alr import input_streams")
    writeLine2(rf)


def writeContextClasses(rf: TextIO, visitor: GrammarVisitor) -> [int]:
    nterminalClasses = generateNterminalClasses(visitor)

    generatedRuleByRuleNum = {}
    constructorClasses = generateConstructorClasses(visitor, generatedRuleByRuleNum)
    funcClasses = generateFuncClasses(visitor, generatedRuleByRuleNum)

    classes = [*nterminalClasses, *generatedRuleByRuleNum.values(), *constructorClasses, *funcClasses, ]
    for class_ in classes:
        class_.write(rf)
        writeLine(rf)

    return generatedRuleByRuleNum.keys()


def clearString(string: str) -> str:
    return string.replace("'", "")


def writeGrammar(rf: TextIO, visitor: GrammarVisitor, rulesNumWithConstructor: [int], table: Table):
    writeLine2(rf, f"terminals = {visitor.terminals}")

    writeLine2(rf, f"skipTerminals = {list(visitor.skipTerminalByName.values())}")

    writeLine2(rf, f"nterminals = {visitor.nterminals}")

    writeLine2(rf, f"rules = {visitor.rules}")

    for i, nterminal in enumerate(visitor.nterminals):
        rulesStr = str([f'rules[{rule.num}]' for rule in nterminal.rules])
        writeLine(rf, f"nterminals[{i}].rules = " + clearString(rulesStr))
    writeLine(rf)

    nterminalConstructors = str([f'{nterminal.name}Context' for nterminal in visitor.nterminals])
    writeLine2(rf, "nterminalConstructors = " + clearString(nterminalConstructors))

    ruleConstructorByNum = str({rule_num: f'_Rule{rule_num}Context' for rule_num in rulesNumWithConstructor})
    writeLine2(rf, "ruleConstructorByNum = " + clearString(ruleConstructorByNum))

    writeLine2(rf, f"ruleAndPosByNum = {visitor.ruleAndPosByNum}")

    writeLine3(rf, f"table = {table}")


def getLexerClassName(grammarName: str) -> str:
    return grammarName + "Lexer"


def writeLexer(rf: TextIO, grammarName: str):
    initMethod = generateInitMethodInfo(["inputStream: input_streams.InputStream"],
                                        ["self._lexer = lexer.lexer(terminals, skipTerminals, inputStream)"])
    nextMethod = MethodInfo("next", args=["self"], returnType=f"{_instancesPackage}.Token",
                            body=["return next(self._lexer)"])

    classLexer = ClassInfo(getLexerClassName(grammarName), parent="lexer.Lexer", methods=[initMethod, nextMethod])
    classLexer.write(rf)

    writeLine(rf)


def writeParser(rf: TextIO, grammarName: str):
    lexerClassName = getLexerClassName(grammarName)
    lexerName = lexerClassName[0].lower() + lexerClassName[1:]
    initMethod = generateInitMethodInfo([f"{lexerName}: {lexerClassName}"], [
        f"self._parser = parser.Parser(nterminals, nterminalConstructors, rules, ruleConstructorByNum, "
        f"ruleAndPosByNum, table, {lexerName})",
        "self._parseCnt = 0"])

    parseMethod = MethodInfo("parse", args=["self", "tree: bool = False"],
                             returnType=f"{_instancesPackage}.NterminalContext",
                             body=["if self._parseCnt != 0:",
                                   "    raise parser.ParserException('parser object can parse only once')",
                                   "self._parseCnt += 1", "return self._parser.parse(tree)"])

    classParser = ClassInfo(f'{grammarName}Parser', methods=[initMethod, parseMethod])
    classParser.write(rf)


def createGrammarFile(visitor: GrammarVisitor, table: Table, directory: str, grammarName: str):
    fileName = getPythonFileName(directory, grammarName, "Grammar")
    with open(fileName, 'w') as rf:
        writeImports(rf)
        writeLine3(rf, "nterminals = None  # for context classes")
        rulesNumWithConstructor = writeContextClasses(rf, visitor)
        writeGrammar(rf, visitor, rulesNumWithConstructor, table)
        writeLexer(rf, grammarName)
        writeParser(rf, grammarName)
