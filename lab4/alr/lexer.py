import re

from alr.input_streams import InputStream
from alr.instances import Terminal, Token, END_TERMINAL_NAME


class LexerException(Exception):
    pass


class Lexer:
    def next(self) -> Token:
        pass


def findMatchInfo(terminals: [Terminal], data: str):
    for terminal in terminals:
        match = re.match(terminal.regexp, data)
        if match:
            return match, terminal
    return None


def lexer(terminals: [Terminal], skip_terminals: [Terminal], input_stream: InputStream) -> Token:
    source = input_stream.source
    len_source = len(source)
    while not input_stream.is_consumed:
        data = input_stream.get()
        match_info = findMatchInfo(skip_terminals, data)
        if match_info:
            match, _ = match_info
            input_stream.consume(match.end())
            continue
        match_info = findMatchInfo(terminals, data)
        if match_info:
            match, terminal = match_info
            end = match.end()
            yield Token(terminal, input_stream.index, input_stream.index + end, source)
            input_stream.consume(end)
            continue
        raise LexerException(f'pos: {input_stream.index}: Can not parse {data}')
    endTerminal = Terminal(END_TERMINAL_NAME, len(terminals))
    yield Token(endTerminal, len_source, len_source, source)
