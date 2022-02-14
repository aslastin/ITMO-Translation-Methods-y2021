import argparse
import sys

from RegexpGrammar import RegexpLexer, RegexpParser
from alr.input_streams import FileStream, InputStream


def initInputStream(file: str):
    if file is None:
        inputGrammar = []
        while line := sys.stdin.readline():
            inputGrammar.append(line)
        return InputStream(''.join(inputGrammar))
    else:
        return FileStream(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Regexp grammar tester")
    parser.add_argument("--file", default=None, type=str, help="file with input")
    parser.add_argument("--tree", type=bool, default=True, help="whether build tree and render it or not")

    args = parser.parse_args()
    file, tree = args.file, args.tree

    inputStream = initInputStream(file)

    lexer = RegexpLexer(inputStream)
    parser = RegexpParser(lexer)

    if tree:
        tree = parser.parse(tree=True)
        tree.render()
    else:
        res = parser.parse()
        print(res.getVertexName())
