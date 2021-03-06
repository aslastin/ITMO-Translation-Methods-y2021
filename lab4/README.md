# ALR

__ALR (Awesome Language Recognizer)__ умеет разбирать грамматики класса _LALR_ и использует восходящий разбор.

Тажке он поддерживает транслириующие символы, наследуемые и синтезируемые атрибуты.

Генератор парсеров _ALR_ был протестирован на грамматиках, перечисленных в папке [test](test).

Чтобы сгенерировать разборщик для одной из них, запустите [alr.py](alr.py) с аргументами, перечисленными в файле `test/<имя грамматики>/build.txt`.

Например, для генерации парсера арифметических выражений используйте аргументы из файла [test/calc/build.txt](test/calc/build.txt):
`--start E --file test/calc/calc.grammar --name Calc --test --dir test/calc`.

Файлы с расширением `.grammar` содержат описание грамматик, которое я попытался сделать максимально простым.
Полный синтаксис для описания грамматик находится в файле [ALR.g4](alr/antlr/ALR.g4)

Для грамматики арифметических выражений [calc.grammar](test/calc/calc.grammar),
на входе `(5*7/5) + (-23) - 5 * (-98-4)/(6*-8-42) + (1 * 2^2^-3 - 5)` автоматически сгенерированный парсер [CalcParser](test/calc/CalcGrammar.py)
построил [следующее](test/calc/parse-tree.pdf) дерево разбора.
