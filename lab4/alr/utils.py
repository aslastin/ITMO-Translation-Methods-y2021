import functools
import os
from typing import TextIO, Optional


def getPythonFileName(directory: str, grammarName: str, suffix: str):
    return os.path.join(directory, grammarName + suffix + ".py")


def write(rf: TextIO, output: Optional[str] = None, tabs: int = 0):
    if output:
        rf.write(''.join(['    ' for _ in range(tabs)]) + output)


def writeMany(rf: TextIO, outputs: [str], tabs: int = 0):
    for output in outputs:
        writeLine(rf, output, tabs)


def writeLineN(linesCnt: int, rf: TextIO, output: Optional[str] = None, tabs: int = 0):
    write(rf, output, tabs)
    rf.write(''.join(["\n" for _ in range(linesCnt)]))


writeLine = functools.partial(writeLineN, 1)
writeLine2 = functools.partial(writeLineN, 2)
writeLine3 = functools.partial(writeLineN, 3)
