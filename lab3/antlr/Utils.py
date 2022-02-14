import Symbols
import Units
from antlrbase.SasParser import SasParser


def get_c_type(type):
    if type == Symbols.TypeEnum.INT:
        return "int"
    elif type == Symbols.TypeEnum.LONG:
        return "ll"
    elif type == Symbols.TypeEnum.DOUBLE:
        return "double"
    elif type == Symbols.TypeEnum.VOID:
        return "void"
    elif type == Symbols.TypeEnum.BOOL:
        return "bool"
    else:
        raise RuntimeError("Unknown type error")

def extract_types(*variables) -> [str]:
    return list(map(lambda arg: str(arg.type), variables))


def resolve_types(type1, type2):
    types = (type1, type2)
    if Symbols.TypeEnum.INVALID in types:
        return Symbols.TypeEnum.INVALID
    elif Symbols.TypeEnum.DOUBLE in types:
        return Symbols.TypeEnum.DOUBLE
    elif Symbols.TypeEnum.LONG in types:
        return Symbols.TypeEnum.LONG
    elif Symbols.TypeEnum.INT in types:
        return Symbols.TypeEnum.INT
    elif Symbols.TypeEnum.BOOL in types:
        return Symbols.TypeEnum.BOOL
    else:
        return Symbols.TypeEnum.INVALID


def _define_gen_tmp_var_name():
    cnt = [0]

    def tmp_var_generator(suffix=None):
        name = f"tmp_{cnt[0]}"
        cnt[0] += 1
        if suffix is not None:
            name += suffix
        return name

    return tmp_var_generator


gen_tmp_var_name = _define_gen_tmp_var_name()


def gen_tmp_var(stype):
    return Symbols.VarSymbol(stype, gen_tmp_var_name())


# Get function's name in C result-file
def resolve_func_name(ret_type, name: str, *args) -> str:
    arg_ts = '_'.join(extract_types(*args))
    f_name = name + "_" + str(ret_type) + ("_" + arg_ts if len(arg_ts) else "")
    if name in Units.GlobalUnit.base_funcs:
        return "___" + f_name
    return "__" + f_name


def resolve_var_name(stype, name: str):
    return f"_{name}_{stype}"


def get_number_type(tokenType):
    if tokenType == SasParser.LONG:
        return Symbols.TypeEnum.LONG
    elif tokenType == SasParser.INT:
        return Symbols.TypeEnum.INT
    elif tokenType == SasParser.DOUBLE:
        return Symbols.TypeEnum.DOUBLE
    else:
        return Symbols.TypeEnum.INVALID
