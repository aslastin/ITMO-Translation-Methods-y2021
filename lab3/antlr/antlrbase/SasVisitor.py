# Generated from Sas.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SasParser import SasParser
else:
    from SasParser import SasParser

# This class defines a complete generic visitor for a parse tree produced by SasParser.

class SasVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SasParser#prog.
    def visitProg(self, ctx:SasParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#StatFunc.
    def visitStatFunc(self, ctx:SasParser.StatFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#StatReturn.
    def visitStatReturn(self, ctx:SasParser.StatReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#StatUnitWithBody.
    def visitStatUnitWithBody(self, ctx:SasParser.StatUnitWithBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#StatAssign.
    def visitStatAssign(self, ctx:SasParser.StatAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#StatExpr.
    def visitStatExpr(self, ctx:SasParser.StatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#func.
    def visitFunc(self, ctx:SasParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprVar.
    def visitExprVar(self, ctx:SasParser.ExprVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprPow.
    def visitExprPow(self, ctx:SasParser.ExprPowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprMult.
    def visitExprMult(self, ctx:SasParser.ExprMultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprFuncCall.
    def visitExprFuncCall(self, ctx:SasParser.ExprFuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprUnary.
    def visitExprUnary(self, ctx:SasParser.ExprUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprNumber.
    def visitExprNumber(self, ctx:SasParser.ExprNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprBool.
    def visitExprBool(self, ctx:SasParser.ExprBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprAdd.
    def visitExprAdd(self, ctx:SasParser.ExprAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprBrackets.
    def visitExprBrackets(self, ctx:SasParser.ExprBracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprAbs.
    def visitExprAbs(self, ctx:SasParser.ExprAbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprAnd.
    def visitExprAnd(self, ctx:SasParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprBaseCall.
    def visitExprBaseCall(self, ctx:SasParser.ExprBaseCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprCmp.
    def visitExprCmp(self, ctx:SasParser.ExprCmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprXor.
    def visitExprXor(self, ctx:SasParser.ExprXorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprOr.
    def visitExprOr(self, ctx:SasParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprNeq.
    def visitExprNeq(self, ctx:SasParser.ExprNeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ExprEq.
    def visitExprEq(self, ctx:SasParser.ExprEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#rightCmp.
    def visitRightCmp(self, ctx:SasParser.RightCmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#opCmp.
    def visitOpCmp(self, ctx:SasParser.OpCmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#UnitIf.
    def visitUnitIf(self, ctx:SasParser.UnitIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#UnitFor.
    def visitUnitFor(self, ctx:SasParser.UnitForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#UnitWhile.
    def visitUnitWhile(self, ctx:SasParser.UnitWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#varList.
    def visitVarList(self, ctx:SasParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#var.
    def visitVar(self, ctx:SasParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#exprList.
    def visitExprList(self, ctx:SasParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#number.
    def visitNumber(self, ctx:SasParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#boolean.
    def visitBoolean(self, ctx:SasParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#f.
    def visitF(self, ctx:SasParser.FContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#t.
    def visitT(self, ctx:SasParser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#If.
    def visitIf(self, ctx:SasParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#IfElse.
    def visitIfElse(self, ctx:SasParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#for_.
    def visitFor_(self, ctx:SasParser.For_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ForStatSeq.
    def visitForStatSeq(self, ctx:SasParser.ForStatSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#ForStatExpr.
    def visitForStatExpr(self, ctx:SasParser.ForStatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#forSeq.
    def visitForSeq(self, ctx:SasParser.ForSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#seq.
    def visitSeq(self, ctx:SasParser.SeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SasParser#while_.
    def visitWhile_(self, ctx:SasParser.While_Context):
        return self.visitChildren(ctx)



del SasParser