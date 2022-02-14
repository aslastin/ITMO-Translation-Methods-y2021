from functools import reduce

import Utils


class Unit:
    pass


class UnitWithBody(Unit):
    def __init__(self):
        super().__init__()
        self.body = []

    def add(self, unit: Unit):
        self.body.append(unit)

    def __str__(self):
        return "\n".join(map(str, self.body))


class ExprUnit(Unit):
    def __init__(self, sym):
        super().__init__()
        self.sym = sym

    def __str__(self):
        return str(self.sym) + ";"


class AssignUnit(Unit):
    def __init__(self, var, sym):
        super().__init__()
        self.var = var
        self.sym = sym

    def __str__(self):
        return str(self.var) + " = " + str(self.sym) + ";"


class AssignDefUnit(AssignUnit):
    def __init__(self, var, sym):
        super().__init__(var, sym)

    def __str__(self):
        return f"{'const' if self.var.is_const else ''} {Utils.get_c_type(self.var.type)} {super().__str__()}"


class VarDeclUnit(Unit):
    def __init__(self, var):
        super().__init__()
        self.var = var

    def __str__(self):
        return f"{'const' if self.var.is_const else ''} {Utils.get_c_type(self.var.type)} {self.var};"


class FuncDeclUnit(Unit):
    def __init__(self, func):
        super().__init__()
        self.func = func

    def __str__(self):
        return str(self.func) + ";"


class IfUnit(UnitWithBody):
    def __init__(self, cond):
        super().__init__()
        self.cond = cond

    def __str__(self):
        return "\n".join([f"if ({self.cond})", "{", super().__str__(), "}"])


class IfElseUnit(Unit):
    def __init__(self, cond):
        super().__init__()
        self.cond = cond
        self.if_unit = UnitWithBody()
        self.else_unit = UnitWithBody()

    def getIfUnit(self):
        return self.if_unit

    def getElseUnit(self):
        return self.else_unit

    def __str__(self):
        return "\n".join([
            f"if ({self.cond})", "{", str(self.if_unit), "}",
            "else", "{", str(self.else_unit), "}"
        ])


class WhileUnit(UnitWithBody):
    def __init__(self, cond):
        super().__init__()
        self.cond = cond

    def __str__(self):
        return "\n".join([f"while ({self.cond})", "{", super().__str__(), "}"])


class FuncDefUnit(UnitWithBody):
    def __init__(self, func_header):
        super().__init__()
        self.func_header = func_header

    def __str__(self):
        return "\n".join([str(self.func_header), "{", super().__str__(), "}"]) + "\n"


class IncludeUnit(Unit):
    def __init__(self, include_file: str):
        super().__init__()
        self.include_file = include_file

    def __str__(self):
        return "#include " + self.include_file


class GlobalUnit(Unit):
    base_includes = {'<stdio.h>', '<string.h>', '<stdbool.h>', '"sasbase.h"'}
    base_funcs = {"pow", "abs", "read", "print", "println"}

    def __init__(self):
        super().__init__()

        self.includeBody = UnitWithBody()
        for includeFile in GlobalUnit.base_includes:
            self.includeBody.add(IncludeUnit(includeFile))

        self.func_decls = UnitWithBody()
        self.func_defs = UnitWithBody()
        self.main = UnitWithBody()

    def __str__(self):
        top = "\n\n".join(map(str, [self.includeBody, self.func_decls, self.func_defs]))
        return top + "\nint main()\n{\n" + str(self.main) + "\n}\n"


class ReturnUnit(Unit):
    def __init__(self, sym):
        super().__init__()
        self.sym = sym

    def __str__(self):
        return f"return {self.sym};"


class ForSeqUnit(Unit):
    def __init__(self, start, step, end, is_inclusive: bool, var, is_var_new):
        super().__init__()
        self.start = start
        self.step = step
        self.end = end
        self.is_inclusive = is_inclusive
        self.var = var
        self.is_var_new = is_var_new

    def __str__(self):
        var = str(self.var)
        tmp_var = Utils.gen_tmp_var(self.step.type)
        return f"{self.var.type if self.is_var_new else ''} {var} = {self.start}, " \
               f"{tmp_var} = {self.step}; " \
               f"{var} {'<=' if self.is_inclusive else '<'} {self.end}; " \
               f"{var} += {tmp_var}"


class ForUnit(UnitWithBody):
    def __init__(self, *syms):
        super().__init__()
        self.syms = syms

    def _str_reducer(self, prev: str, cur):
        return f"for ({cur})\n{{\n {prev} \n}}" if isinstance(cur, ForSeqUnit) else f"if ({cur})\n{{\n {prev} \n}}"

    def __str__(self):
        return reduce(self._str_reducer, reversed(self.syms), super().__str__())
