from typing import TextIO

from alr.utils import writeLine, writeLine2, writeLine3, getPythonFileName, writeMany


def writeImports(rf: TextIO, grammarName: str):
    writeLine(rf, "import argparse")
    writeLine2(rf, "import sys")
    writeLine(rf, f"from {grammarName}Grammar import {grammarName}Lexer, {grammarName}Parser")
    writeLine3(rf, "from alr.input_streams import FileStream, InputStream")


def writeInitInputStream(rf: TextIO):
    writeLine(rf, "def initInputStream(file: str):")
    writeLine(rf, "if file is None:", tabs=1)
    writeLine(rf, "inputGrammar = []", tabs=2)
    writeLine(rf, "while line := sys.stdin.readline():", tabs=2)
    writeLine(rf, "inputGrammar.append(line)", tabs=3)
    writeLine(rf, "return InputStream(''.join(inputGrammar))", tabs=2)
    writeLine(rf, "else:", tabs=1)
    writeLine3(rf, "return FileStream(file)", tabs=2)


def writeMain(rf: TextIO, grammarName: str):
    writeLine(rf, "if __name__ == '__main__':")
    block = [
        f'parser = argparse.ArgumentParser(description="{grammarName} grammar tester")',
        'parser.add_argument("--file", default=None, type=str, help="file with input")',
        'parser.add_argument("--tree", type=bool, default=True, help="whether build tree and render it or not")'
    ]
    writeMany(rf, block, tabs=1)
    writeLine(rf)

    block = [
        'args = parser.parse_args()',
        'file, tree = args.file, args.tree'
    ]
    writeMany(rf, block, tabs=1)
    writeLine(rf)

    writeLine2(rf, 'inputStream = initInputStream(file)', tabs=1)

    block = [
        f'lexer = {grammarName}Lexer(inputStream)',
        f'parser = {grammarName}Parser(lexer)',
    ]
    writeMany(rf, block, tabs=1)
    writeLine(rf)

    writeLine(rf, "if tree:", tabs=1)
    writeLine(rf, "tree = parser.parse(tree=True)", tabs=2)
    writeLine(rf, "tree.render()", tabs=2)
    writeLine(rf, "else:", tabs=1)
    writeLine(rf, "res = parser.parse()", tabs=2)
    writeLine(rf, "print(res.getVertexName())", tabs=2)


def createTestFile(directory: str, grammarName: str):
    fileName = getPythonFileName(directory, grammarName, "Test")
    with open(fileName, 'w') as rf:
        writeImports(rf, grammarName)
        writeInitInputStream(rf)
        writeMain(rf, grammarName)
