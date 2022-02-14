from antlr4 import *

import Symbols
import Units
import Utils


class Scope:
    pass


class VarScope(Scope):
    # enclosing_scope : VarScope
    def __init__(self, unit: Units.UnitWithBody, enclosing_scope=None):
        self.unit = unit
        self.enclosing_scope = enclosing_scope
        self.all_vars: dict[str, {Symbols.TypeEnum}] = {}
        self.cur_vars: dict[str, Symbols.TypeEnum] = {}
        self.const_vars: {str} = set()

    def getEnclosingScope(self):
        return self.enclosing_scope

    def getUnit(self):
        return self.unit

    def getCurType(self, name):
        return self.cur_vars.get(name)

    def getAllTypes(self, name):
        return self.all_vars.get(name)

    def is_const_var(self, name):
        return name in self.const_vars

    def define(self, var: Symbols.VarSymbol):
        scope = self.resolve(var.name)
        if scope is None:
            scope = self
        scope._define(var)

    def _define(self, var: Symbols.VarSymbol):
        name, vtype, is_const = var.name, var.type, var.is_const
        if is_const and name in self.cur_vars:
            raise RuntimeError(f"Const var was already defined: {var}")
        self.cur_vars[name] = vtype
        if name not in self.all_vars:
            self.all_vars[name] = set()
        self.all_vars[name].add(vtype)
        if is_const:
            self.const_vars.add(name)

    # (current type, all types, is const, it's scope)
    def resolve(self, name: str):
        vtype = self.cur_vars.get(name)
        if vtype is not None:
            return self
        if self.enclosing_scope is not None:
            return self.enclosing_scope.resolve(name)
        return None


class FuncScope(Scope):
    def __init__(self):
        self.funcs = set()

    def define(self, func_sym: Symbols.FuncSymbol):
        f_name = Utils.resolve_func_name(func_sym.type, func_sym.name, *func_sym.args)
        if f_name in self.funcs:
            raise RuntimeError(f"@ Function redefinition {f_name}@")
        self.funcs.add(f_name)

    def resolve(self, func_sym: Symbols.FuncSymbol):
        return Utils.resolve_func_name(func_sym.type, func_sym.name, *func_sym.args) in self.funcs
