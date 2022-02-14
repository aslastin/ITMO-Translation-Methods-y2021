from enum import Enum

import Utils


class TypeEnum(Enum):
    INVALID = 1
    VOID = 2
    INT = 3
    LONG = 4
    DOUBLE = 5
    BOOL = 6

    def __str__(self):
        return super().__str__()[len("TypeEnum."):].lower()


# Symbol - something that has type (eg: variables, function headers)

class Symbol:
    def __init__(self, stype=TypeEnum.INVALID):
        self.type = stype


class VarSymbol(Symbol):
    def __init__(self, stype: TypeEnum, name: str, is_const=False):
        super().__init__(stype)
        self.name = name
        self.is_const = is_const

    def __str__(self):
        return Utils.resolve_var_name(self.type, self.name)


class FuncSymbol(Symbol):
    def __init__(self, ret_type: TypeEnum, name: str, *args: Symbol):
        super().__init__(ret_type)
        self.name = name
        self.args = args

    def __str__(self):
        return Utils.resolve_func_name(self.type, self.name, *self.args)


class FuncCallSymbol(FuncSymbol):
    def __init__(self, ret_type, name, *args: Symbol):
        super().__init__(ret_type, name, *args)

    def __str__(self):
        return f"{super().__str__()}({', '.join(map(str, self.args))})"


class FuncHeaderSymbol(FuncSymbol):
    def __init__(self, ret_type, name, *args: VarSymbol):
        super().__init__(ret_type, name, *args)

    def __str__(self):
        typed_args = ', '.join(map(lambda arg: str(arg.type) + ' ' + str(arg), self.args))
        return f"{Utils.get_c_type(self.type)} {super().__str__()}({typed_args})"


class NumberSymbol(Symbol):
    def __init__(self, stype, value: str):
        super().__init__(stype)
        self.value = value

    def __str__(self):
        return self.value


class BoolSymbol(Symbol):
    def __init__(self, value: str):
        super().__init__(TypeEnum.BOOL)
        self.value = value

    def __str__(self):
        return self.value


class BracketsSymbol(Symbol):
    def __init__(self, stype, brackets=False):
        super().__init__(stype)
        self.brackets = brackets

    def __str__(self):
        strval = self._toString()
        if self.brackets:
            return "(" + strval + ")"
        return strval

    def _toString(self):
        pass


class UnaryOpSymbol(BracketsSymbol):
    def __init__(self, op: str, arg: Symbol, brackets=False):
        super().__init__(arg.type, brackets)
        self.op = op
        self.arg = arg

    def _toString(self):
        return self.op + str(self.arg)


class BinaryOpSymbol(BracketsSymbol):
    def __init__(self, op: str, arg1: Symbol, arg2: Symbol, brackets=False):
        super().__init__(Utils.resolve_types(arg1.type, arg2.type), brackets)
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2

    def _toString(self):
        return str(self.arg1) + self.op + str(self.arg2)


class BinaryLogicOpSymbol(BracketsSymbol):
    def __init__(self, op: str, arg1: Symbol, arg2: Symbol, brackets=False, cast_args_bool=False):
        super().__init__(TypeEnum.BOOL, brackets)
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self._cast_args_bool = cast_args_bool

    @staticmethod
    def _argToStringBool(arg: Symbol):
        strval = str(arg)
        if arg.type != TypeEnum.BOOL:
            return f'((bool) {strval})'
        return strval

    def _argToString(self, arg):
        return BinaryLogicOpSymbol._argToStringBool(arg) if self._cast_args_bool else str(arg)

    def _toString(self):
        return self._argToString(self.arg1) + self.op + self._argToString(self.arg2)
