import argparse
import errno
import os
import sys

from antlr4 import InputStream, FileStream

from alr.antlr.ALRLexer import ALRLexer, CommonTokenStream
from alr.antlr.ALRParser import ALRParser
from alr.grammar_file import createGrammarFile
from alr.grammar_visitor import GrammarVisitor, GrammarException
from alr.table_creator import TableGenerator
from alr.test_file import createTestFile


def initInputStream(file):
    if file is None:
        inputGrammar = []
        while line := sys.stdin.readline():
            inputGrammar.append(line)
        return InputStream(''.join(inputGrammar))
    else:
        return FileStream(file)


def createDirectory(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="ALR grammar compiler")
    parser.add_argument("--start", type=str, help="name of the starting nterminal")
    parser.add_argument("--file", default=None, type=str, help="file with grammar")
    parser.add_argument("--name", default="Res", type=str, help="name of the grammar")
    parser.add_argument("--test", action='store_true', help="whether generate test code or not")
    parser.add_argument("--dir", default='', type=str,
                        help="output directory, where all generated files will be stored")

    args = parser.parse_args()
    start, file, grammar_name, test, directory = args.start, args.file, args.name, args.test, args.dir

    input_stream = initInputStream(file)

    lexer = ALRLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ALRParser(token_stream)
    tree = parser.start()

    visitor = GrammarVisitor(start)
    try:
        visitor.visit(tree)
    except GrammarException as e:
        sys.stderr.write(str(e))
        exit(1)

    table = TableGenerator(visitor).generate()

    directory = os.path.join(os.getcwd(), directory)
    createDirectory(directory)

    createGrammarFile(visitor, table, directory, grammar_name)

    if test:
        createTestFile(directory, grammar_name)
