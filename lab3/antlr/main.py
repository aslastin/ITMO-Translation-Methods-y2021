import sys
from functools import reduce

from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.error.ErrorListener import ErrorListener

import Symbols
import Utils
from Scopes import VarScope, FuncScope
from Symbols import NumberSymbol, BoolSymbol, BinaryOpSymbol, UnaryOpSymbol, FuncCallSymbol, \
    BinaryLogicOpSymbol, VarSymbol, FuncHeaderSymbol
from Units import GlobalUnit, ReturnUnit, AssignDefUnit, AssignUnit, VarDeclUnit, ExprUnit, FuncDefUnit, \
    ForUnit, IfElseUnit, IfUnit, WhileUnit, ForSeqUnit
from antlrbase.SasLexer import SasLexer
from antlrbase.SasListener import SasListener
from antlrbase.SasParser import SasParser
from antlrbase.SasVisitor import SasVisitor


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self._error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self._error = True

    def wasError(self):
        return self._error


class FuncGathererListener(SasListener):
    def __init__(self):
        self.funcs = {}

    def exitFunc(self, ctx: SasParser.FuncContext):
        f_name = ctx.ID().getText()
        if f_name in self.funcs:
            raise RuntimeError(f"@ Only unique funcs allowed: {f_name} @\n{ctx.getText()}")
        var_list = ctx.varList()
        self.funcs[f_name] = (ctx, 0 if var_list is None else len(var_list.var()))


class CLangConverterVisitor(SasVisitor):
    def __init__(self, global_unit: GlobalUnit, funcs):
        super().__init__()
        self.global_unit = global_unit
        self.funcs = funcs
        self.cur_unit = global_unit.main
        self.func_scope = global_unit.func_scope
        self.var_scope = global_unit.var_scope
        self.func_header = None
        self.ret_cnt = None

    def _visitAll(self, toVisitContexts: [ParserRuleContext]):
        for ctx in toVisitContexts:
            self.visit(ctx)

    def _visitNext(self, new_unit, next):
        prev_unit, prev_var_scope = self.cur_unit, self.var_scope
        self.cur_unit = new_unit
        self.var_scope = VarScope(new_unit, prev_var_scope)
        self.visit(next)
        prev_unit.add(new_unit)
        self.cur_unit, self.var_scope = prev_unit, prev_var_scope

    def visitProg(self, ctx: SasParser.ProgContext):
        self._visitAll(ctx.stat())

    def visitStatFunc(self, ctx: SasParser.StatFuncContext):
        self.visit(ctx.func())

    def visitStatReturn(self, ctx: SasParser.StatReturnContext):
        if self.func_header.type == Symbols.TypeEnum.VOID:
            raise RuntimeError(f"@ function {self.func_header.name} has return, "
                               f"but no return type was provided @\n {ctx.getText()}")
        self.ret_cnt += 1
        self.cur_unit.add(ReturnUnit(self.visit(ctx.expr())))

    def visitStatUnitWithBody(self, ctx: SasParser.StatUnitWithBodyContext):
        self.visit(ctx.unitWithBody())

    def visitStatAssign(self, ctx: SasParser.StatAssignContext):
        is_const = ctx.const is not None
        varList = [var.getText() for var in ctx.varList().var()]
        exprList = [self.visit(e) for e in ctx.exprList().expr()]

        if len(varList) != len(exprList):
            raise RuntimeError(f"@ Different number of arguments when assigning: {ctx.getText()} @")

        for var, expr in zip(varList, exprList):
            cur_var_scope = self.var_scope.resolve(var)

            if cur_var_scope is not None and cur_var_scope.is_const_var(var):
                raise RuntimeError(f"@ Cannot reinitialize const variable {var}: {ctx.getText()} @")
            if is_const and cur_var_scope is not None:
                raise RuntimeError(f"@ variable({var}) without const was already defined: {ctx.getText()} @")

            tmp_var = Utils.gen_tmp_var(expr.type)
            self.cur_unit.add(AssignDefUnit(tmp_var, expr))

            cur_var = VarSymbol(expr.type, var, is_const)

            if cur_var_scope is not None:
                if expr.type not in cur_var_scope.getAllTypes(var):
                    cur_var_scope.getUnit().add(VarDeclUnit(cur_var))
                cur_var_scope.define(cur_var)
                self.cur_unit.add(AssignUnit(cur_var, tmp_var))
            else:
                self.cur_unit.add(AssignDefUnit(cur_var, tmp_var))
                self.var_scope.define(cur_var)

    def visitStatExpr(self, ctx: SasParser.StatExprContext):
        self.cur_unit.add(ExprUnit(self.visit(ctx.expr())))

    def visitFunc(self, ctx: SasParser.FuncContext):
        if self.func_header is None:
            return
        self.visit(ctx.prog())

    def visitF(self, ctx: SasParser.FContext):
        name = ctx.ID().getText()
        t = Symbols.TypeEnum.INVALID
        if ctx.t() is None:
            t = Symbols.TypeEnum.VOID
        else:
            str_t = ctx.t().ID().getText()
            if str_t == "int":
                t = Symbols.TypeEnum.INT
            elif str_t == "double":
                t = Symbols.TypeEnum.DOUBLE
            elif str_t == "long":
                t = Symbols.TypeEnum.LONG
            elif str_t == "bool":
                t = Symbols.TypeEnum.BOOL
        return VarSymbol(t, name)

    def visitExprFuncCall(self, ctx: SasParser.ExprFuncCallContext):
        f = self.visit(ctx.f())
        if f.type == Symbols.TypeEnum.INVALID:
            raise RuntimeError(f"@ Called function {f.name} with UNKNOWN type @\n{ctx.getText()}")

        args = []
        if ctx.exprList() is not None:
            args = [self.visit(e) for e in ctx.exprList().expr()]

        res = FuncCallSymbol(f.type, f.name, *args)

        if f.name in GlobalUnit.base_funcs:
            return res

        f_ctx, args_cnt = self.funcs[f.name]

        if args_cnt != len(args):
            raise RuntimeError(
                f"@ Expected {args_cnt} args for {f.name}, but found {len(args)}: {ctx.getText()} @")

        header_vars = []
        if args_cnt > 0:
            arg_names = [name.getText() for name in f_ctx.varList().var()]
            header_vars = [VarSymbol(arg.type, name) for arg, name in zip(args, arg_names)]

        func_header = FuncHeaderSymbol(f.type, f.name, *header_vars)

        if not self.func_scope.resolve(func_header):
            self.func_scope.define(func_header)

            prev_func_header, prev_ret_cnt = self.func_header, self.ret_cnt

            self.global_unit.func_decls.add(ExprUnit(func_header))
            func_def = FuncDefUnit(func_header)
            self.global_unit.func_defs.add(func_def)

            prev_unit, prev_var_scope = self.cur_unit, self.var_scope

            self.cur_unit = func_def
            self.var_scope = VarScope(func_def)
            for var in func_header.args:
                self.var_scope.define(var)

            self.func_header = func_header
            self.ret_cnt = 0
            self.visit(f_ctx)
            if self.ret_cnt == 0 and self.func_header.type != Symbols.TypeEnum.VOID:
                raise RuntimeError(f"@ function {self.func_header.name} has void type, "
                                   f"but return type was {self.func_header.type} @")
            self.cur_unit, self.var_scope = prev_unit, prev_var_scope
            self.func_header, self.ret_cnt = prev_func_header, prev_ret_cnt
        return res

    def visitExprBrackets(self, ctx: SasParser.ExprBracketsContext):
        return UnaryOpSymbol("", self.visit(ctx.expr()), brackets=True)

    def visitExprAbs(self, ctx: SasParser.ExprAbsContext):
        e = self.visit(ctx.exprBase())
        return FuncCallSymbol(e.type, "abs", e)

    def visitExprPow(self, ctx: SasParser.ExprPowContext):
        e1, e2 = self.visit(ctx.e1), self.visit(ctx.e2)
        return FuncCallSymbol(Utils.resolve_types(e1.type, e2.type), "pow", e1, e2)

    def visitExprUnary(self, ctx: SasParser.ExprUnaryContext):
        return UnaryOpSymbol(ctx.op.text, self.visit(ctx.exprBase()))

    def visitExprMult(self, ctx: SasParser.ExprMultContext):
        return BinaryOpSymbol(ctx.op.text, self.visit(ctx.e1), self.visit(ctx.e2))

    def visitExprAdd(self, ctx: SasParser.ExprAddContext):
        return BinaryOpSymbol(ctx.op.text, self.visit(ctx.e1), self.visit(ctx.e2))

    def visitExprBool(self, ctx: SasParser.ExprBoolContext):
        return BoolSymbol(ctx.getText())

    def visitExprVar(self, ctx: SasParser.ExprVarContext):
        name = ctx.var().getText()
        scope = self.var_scope.resolve(name)
        if scope is None:
            raise RuntimeError(f"@ No such variable: {name} @")
        return VarSymbol(scope.getCurType(name), name)

    def visitExprNumber(self, ctx: SasParser.ExprNumberContext):
        num = ctx.number()
        return NumberSymbol(Utils.get_number_type(num.start.type), num.getText())

    def visitExprBaseCall(self, ctx: SasParser.ExprBaseCallContext):
        return self.visit(ctx.exprBase())

    def visitExprCmp(self, ctx: SasParser.ExprCmpContext):
        right_cmps = ctx.rightCmp()
        ln = len(right_cmps)
        e_start, e_end = self.visit(ctx.exprBase()), self.visit(right_cmps[ln - 1].exprBase())
        if ln > 1:
            right_parts = [self.visit(right_cmp.exprBase()) for right_cmp in right_cmps[:ln - 1]]

            to_cmp = [e_start]
            for right_part in right_parts:
                tmp_var = Utils.gen_tmp_var(right_part.type)
                self.cur_unit.add(AssignDefUnit(tmp_var, right_part))
                to_cmp.append(tmp_var)
            to_cmp.append(e_end)

            res = [BinaryLogicOpSymbol(right_cmps[i].opCmp().getText(), to_cmp[i], to_cmp[i + 1]) for i in range(ln)]
            return reduce(lambda x, y: BinaryLogicOpSymbol("&", x, y), res)
        return BinaryLogicOpSymbol(right_cmps[0].opCmp().getText(), e_start, e_end)

    def visitExprEq(self, ctx: SasParser.ExprEqContext):
        args = [self.visit(e) for e in ctx.exprBase()]
        tmp_var = Utils.gen_tmp_var(args[0].type)
        self.cur_unit.add(AssignDefUnit(tmp_var, args[0]))
        wrap_eq = lambda x, y: BinaryLogicOpSymbol("==", x, y)
        reduce_eq = lambda acc, cur: BinaryLogicOpSymbol("&", acc, wrap_eq(tmp_var, cur))
        return reduce(reduce_eq, args[2:], wrap_eq(tmp_var, args[1]))

    def visitExprNeq(self, ctx: SasParser.ExprNeqContext):
        return BinaryLogicOpSymbol("!=", self.visit(ctx.e1), self.visit(ctx.e2))

    def visitExprAnd(self, ctx: SasParser.ExprAndContext):
        return BinaryLogicOpSymbol("&", self.visit(ctx.e1), self.visit(ctx.e2), cast_args_bool=True)

    def visitExprXor(self, ctx: SasParser.ExprXorContext):
        return BinaryLogicOpSymbol("^", self.visit(ctx.e1), self.visit(ctx.e2), cast_args_bool=True)

    def visitExprOr(self, ctx: SasParser.ExprOrContext):
        return BinaryLogicOpSymbol("|", self.visit(ctx.e1), self.visit(ctx.e2), cast_args_bool=True)

    def visitUnitIf(self, ctx: SasParser.UnitIfContext):
        self.visit(ctx.if_())

    def visitUnitFor(self, ctx: SasParser.UnitForContext):
        self.visit(ctx.for_())

    def visitUnitWhile(self, ctx: SasParser.UnitWhileContext):
        self.visit(ctx.while_())

    def visitIf(self, ctx: SasParser.IfContext):
        cond = self.visit(ctx.expr())
        self._visitNext(IfUnit(cond), ctx.prog())

    def visitIfElse(self, ctx: SasParser.IfElseContext):
        cond = self.visit(ctx.expr())
        unit = IfElseUnit(cond)

        prev_unit, prev_var_scope = self.cur_unit, self.var_scope

        if_unit = unit.getIfUnit()
        self.cur_unit = if_unit
        self.var_scope = VarScope(if_unit, prev_var_scope)
        self.visit(ctx.prog(0))

        else_unit = unit.getElseUnit()
        self.cur_unit = else_unit
        self.var_scope = VarScope(else_unit, prev_var_scope)
        self.visit(ctx.prog(1))

        prev_unit.add(unit)
        self.cur_unit, self.var_scope = prev_unit, prev_var_scope

    def visitFor_(self, ctx: SasParser.For_Context):
        prev_unit, prev_var_scope = self.cur_unit, self.var_scope
        self.cur_unit = ForUnit()
        self.var_scope = VarScope(self.cur_unit, prev_var_scope)

        syms = [self.visit(ctx.forSeq())]
        syms += [self.visit(stat) for stat in ctx.forStat()]
        self.cur_unit.syms = syms
        self.visit(ctx.prog())

        prev_unit.add(self.cur_unit)
        self.cur_unit, self.var_scope = prev_unit, prev_var_scope

    def visitForStatSeq(self, ctx: SasParser.ForStatSeqContext):
        return self.visit(ctx.forSeq())

    def visitForStatExpr(self, ctx: SasParser.ForStatExprContext):
        return self.visit(ctx.expr())

    def visitForSeq(self, ctx: SasParser.ForSeqContext):
        start, end = self.visit(ctx.seq().start), self.visit(ctx.seq().end)
        follow = ctx.seq().follow

        step = NumberSymbol(Symbols.TypeEnum.INT, "1") if follow is None else \
            BinaryOpSymbol("-", self.visit(follow), start)

        var_name = ctx.var().getText()
        var = VarSymbol(Symbols.TypeEnum.INT, var_name)
        is_new_var = self.var_scope.resolve(var_name) is None
        if is_new_var:
            self.var_scope.define(var)
        return ForSeqUnit(start, step, end, ctx.seq().lb.text == "]", var, is_new_var)

    def visitWhile_(self, ctx: SasParser.While_Context):
        cond = self.visit(ctx.expr())
        self._visitNext(WhileUnit(cond), ctx.prog())


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = SasLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SasParser(token_stream)

    syntaxErrorListener = SyntaxErrorListener()
    parser.addErrorListener(syntaxErrorListener)

    tree = parser.prog()
    if syntaxErrorListener.wasError():
        exit(1)

    listener = FuncGathererListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    global_unit = GlobalUnit()
    global_unit.func_scope = FuncScope()
    global_unit.var_scope = VarScope(global_unit.main)
    visitor = CLangConverterVisitor(global_unit, listener.funcs)
    try:
        visitor.visit(tree)
    except RuntimeError as e:
        sys.stderr.write(str(e))
        exit(1)

    print(global_unit)
