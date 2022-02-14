# Generated from Sas.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SasParser import SasParser
else:
    from SasParser import SasParser

# This class defines a complete listener for a parse tree produced by SasParser.
class SasListener(ParseTreeListener):

    # Enter a parse tree produced by SasParser#prog.
    def enterProg(self, ctx:SasParser.ProgContext):
        pass

    # Exit a parse tree produced by SasParser#prog.
    def exitProg(self, ctx:SasParser.ProgContext):
        pass


    # Enter a parse tree produced by SasParser#StatFunc.
    def enterStatFunc(self, ctx:SasParser.StatFuncContext):
        pass

    # Exit a parse tree produced by SasParser#StatFunc.
    def exitStatFunc(self, ctx:SasParser.StatFuncContext):
        pass


    # Enter a parse tree produced by SasParser#StatReturn.
    def enterStatReturn(self, ctx:SasParser.StatReturnContext):
        pass

    # Exit a parse tree produced by SasParser#StatReturn.
    def exitStatReturn(self, ctx:SasParser.StatReturnContext):
        pass


    # Enter a parse tree produced by SasParser#StatUnitWithBody.
    def enterStatUnitWithBody(self, ctx:SasParser.StatUnitWithBodyContext):
        pass

    # Exit a parse tree produced by SasParser#StatUnitWithBody.
    def exitStatUnitWithBody(self, ctx:SasParser.StatUnitWithBodyContext):
        pass


    # Enter a parse tree produced by SasParser#StatAssign.
    def enterStatAssign(self, ctx:SasParser.StatAssignContext):
        pass

    # Exit a parse tree produced by SasParser#StatAssign.
    def exitStatAssign(self, ctx:SasParser.StatAssignContext):
        pass


    # Enter a parse tree produced by SasParser#StatExpr.
    def enterStatExpr(self, ctx:SasParser.StatExprContext):
        pass

    # Exit a parse tree produced by SasParser#StatExpr.
    def exitStatExpr(self, ctx:SasParser.StatExprContext):
        pass


    # Enter a parse tree produced by SasParser#func.
    def enterFunc(self, ctx:SasParser.FuncContext):
        pass

    # Exit a parse tree produced by SasParser#func.
    def exitFunc(self, ctx:SasParser.FuncContext):
        pass


    # Enter a parse tree produced by SasParser#ExprVar.
    def enterExprVar(self, ctx:SasParser.ExprVarContext):
        pass

    # Exit a parse tree produced by SasParser#ExprVar.
    def exitExprVar(self, ctx:SasParser.ExprVarContext):
        pass


    # Enter a parse tree produced by SasParser#ExprPow.
    def enterExprPow(self, ctx:SasParser.ExprPowContext):
        pass

    # Exit a parse tree produced by SasParser#ExprPow.
    def exitExprPow(self, ctx:SasParser.ExprPowContext):
        pass


    # Enter a parse tree produced by SasParser#ExprMult.
    def enterExprMult(self, ctx:SasParser.ExprMultContext):
        pass

    # Exit a parse tree produced by SasParser#ExprMult.
    def exitExprMult(self, ctx:SasParser.ExprMultContext):
        pass


    # Enter a parse tree produced by SasParser#ExprFuncCall.
    def enterExprFuncCall(self, ctx:SasParser.ExprFuncCallContext):
        pass

    # Exit a parse tree produced by SasParser#ExprFuncCall.
    def exitExprFuncCall(self, ctx:SasParser.ExprFuncCallContext):
        pass


    # Enter a parse tree produced by SasParser#ExprUnary.
    def enterExprUnary(self, ctx:SasParser.ExprUnaryContext):
        pass

    # Exit a parse tree produced by SasParser#ExprUnary.
    def exitExprUnary(self, ctx:SasParser.ExprUnaryContext):
        pass


    # Enter a parse tree produced by SasParser#ExprNumber.
    def enterExprNumber(self, ctx:SasParser.ExprNumberContext):
        pass

    # Exit a parse tree produced by SasParser#ExprNumber.
    def exitExprNumber(self, ctx:SasParser.ExprNumberContext):
        pass


    # Enter a parse tree produced by SasParser#ExprBool.
    def enterExprBool(self, ctx:SasParser.ExprBoolContext):
        pass

    # Exit a parse tree produced by SasParser#ExprBool.
    def exitExprBool(self, ctx:SasParser.ExprBoolContext):
        pass


    # Enter a parse tree produced by SasParser#ExprAdd.
    def enterExprAdd(self, ctx:SasParser.ExprAddContext):
        pass

    # Exit a parse tree produced by SasParser#ExprAdd.
    def exitExprAdd(self, ctx:SasParser.ExprAddContext):
        pass


    # Enter a parse tree produced by SasParser#ExprBrackets.
    def enterExprBrackets(self, ctx:SasParser.ExprBracketsContext):
        pass

    # Exit a parse tree produced by SasParser#ExprBrackets.
    def exitExprBrackets(self, ctx:SasParser.ExprBracketsContext):
        pass


    # Enter a parse tree produced by SasParser#ExprAbs.
    def enterExprAbs(self, ctx:SasParser.ExprAbsContext):
        pass

    # Exit a parse tree produced by SasParser#ExprAbs.
    def exitExprAbs(self, ctx:SasParser.ExprAbsContext):
        pass


    # Enter a parse tree produced by SasParser#ExprAnd.
    def enterExprAnd(self, ctx:SasParser.ExprAndContext):
        pass

    # Exit a parse tree produced by SasParser#ExprAnd.
    def exitExprAnd(self, ctx:SasParser.ExprAndContext):
        pass


    # Enter a parse tree produced by SasParser#ExprBaseCall.
    def enterExprBaseCall(self, ctx:SasParser.ExprBaseCallContext):
        pass

    # Exit a parse tree produced by SasParser#ExprBaseCall.
    def exitExprBaseCall(self, ctx:SasParser.ExprBaseCallContext):
        pass


    # Enter a parse tree produced by SasParser#ExprCmp.
    def enterExprCmp(self, ctx:SasParser.ExprCmpContext):
        pass

    # Exit a parse tree produced by SasParser#ExprCmp.
    def exitExprCmp(self, ctx:SasParser.ExprCmpContext):
        pass


    # Enter a parse tree produced by SasParser#ExprXor.
    def enterExprXor(self, ctx:SasParser.ExprXorContext):
        pass

    # Exit a parse tree produced by SasParser#ExprXor.
    def exitExprXor(self, ctx:SasParser.ExprXorContext):
        pass


    # Enter a parse tree produced by SasParser#ExprOr.
    def enterExprOr(self, ctx:SasParser.ExprOrContext):
        pass

    # Exit a parse tree produced by SasParser#ExprOr.
    def exitExprOr(self, ctx:SasParser.ExprOrContext):
        pass


    # Enter a parse tree produced by SasParser#ExprNeq.
    def enterExprNeq(self, ctx:SasParser.ExprNeqContext):
        pass

    # Exit a parse tree produced by SasParser#ExprNeq.
    def exitExprNeq(self, ctx:SasParser.ExprNeqContext):
        pass


    # Enter a parse tree produced by SasParser#ExprEq.
    def enterExprEq(self, ctx:SasParser.ExprEqContext):
        pass

    # Exit a parse tree produced by SasParser#ExprEq.
    def exitExprEq(self, ctx:SasParser.ExprEqContext):
        pass


    # Enter a parse tree produced by SasParser#rightCmp.
    def enterRightCmp(self, ctx:SasParser.RightCmpContext):
        pass

    # Exit a parse tree produced by SasParser#rightCmp.
    def exitRightCmp(self, ctx:SasParser.RightCmpContext):
        pass


    # Enter a parse tree produced by SasParser#opCmp.
    def enterOpCmp(self, ctx:SasParser.OpCmpContext):
        pass

    # Exit a parse tree produced by SasParser#opCmp.
    def exitOpCmp(self, ctx:SasParser.OpCmpContext):
        pass


    # Enter a parse tree produced by SasParser#UnitIf.
    def enterUnitIf(self, ctx:SasParser.UnitIfContext):
        pass

    # Exit a parse tree produced by SasParser#UnitIf.
    def exitUnitIf(self, ctx:SasParser.UnitIfContext):
        pass


    # Enter a parse tree produced by SasParser#UnitFor.
    def enterUnitFor(self, ctx:SasParser.UnitForContext):
        pass

    # Exit a parse tree produced by SasParser#UnitFor.
    def exitUnitFor(self, ctx:SasParser.UnitForContext):
        pass


    # Enter a parse tree produced by SasParser#UnitWhile.
    def enterUnitWhile(self, ctx:SasParser.UnitWhileContext):
        pass

    # Exit a parse tree produced by SasParser#UnitWhile.
    def exitUnitWhile(self, ctx:SasParser.UnitWhileContext):
        pass


    # Enter a parse tree produced by SasParser#varList.
    def enterVarList(self, ctx:SasParser.VarListContext):
        pass

    # Exit a parse tree produced by SasParser#varList.
    def exitVarList(self, ctx:SasParser.VarListContext):
        pass


    # Enter a parse tree produced by SasParser#var.
    def enterVar(self, ctx:SasParser.VarContext):
        pass

    # Exit a parse tree produced by SasParser#var.
    def exitVar(self, ctx:SasParser.VarContext):
        pass


    # Enter a parse tree produced by SasParser#exprList.
    def enterExprList(self, ctx:SasParser.ExprListContext):
        pass

    # Exit a parse tree produced by SasParser#exprList.
    def exitExprList(self, ctx:SasParser.ExprListContext):
        pass


    # Enter a parse tree produced by SasParser#number.
    def enterNumber(self, ctx:SasParser.NumberContext):
        pass

    # Exit a parse tree produced by SasParser#number.
    def exitNumber(self, ctx:SasParser.NumberContext):
        pass


    # Enter a parse tree produced by SasParser#boolean.
    def enterBoolean(self, ctx:SasParser.BooleanContext):
        pass

    # Exit a parse tree produced by SasParser#boolean.
    def exitBoolean(self, ctx:SasParser.BooleanContext):
        pass


    # Enter a parse tree produced by SasParser#f.
    def enterF(self, ctx:SasParser.FContext):
        pass

    # Exit a parse tree produced by SasParser#f.
    def exitF(self, ctx:SasParser.FContext):
        pass


    # Enter a parse tree produced by SasParser#t.
    def enterT(self, ctx:SasParser.TContext):
        pass

    # Exit a parse tree produced by SasParser#t.
    def exitT(self, ctx:SasParser.TContext):
        pass


    # Enter a parse tree produced by SasParser#If.
    def enterIf(self, ctx:SasParser.IfContext):
        pass

    # Exit a parse tree produced by SasParser#If.
    def exitIf(self, ctx:SasParser.IfContext):
        pass


    # Enter a parse tree produced by SasParser#IfElse.
    def enterIfElse(self, ctx:SasParser.IfElseContext):
        pass

    # Exit a parse tree produced by SasParser#IfElse.
    def exitIfElse(self, ctx:SasParser.IfElseContext):
        pass


    # Enter a parse tree produced by SasParser#for_.
    def enterFor_(self, ctx:SasParser.For_Context):
        pass

    # Exit a parse tree produced by SasParser#for_.
    def exitFor_(self, ctx:SasParser.For_Context):
        pass


    # Enter a parse tree produced by SasParser#ForStatSeq.
    def enterForStatSeq(self, ctx:SasParser.ForStatSeqContext):
        pass

    # Exit a parse tree produced by SasParser#ForStatSeq.
    def exitForStatSeq(self, ctx:SasParser.ForStatSeqContext):
        pass


    # Enter a parse tree produced by SasParser#ForStatExpr.
    def enterForStatExpr(self, ctx:SasParser.ForStatExprContext):
        pass

    # Exit a parse tree produced by SasParser#ForStatExpr.
    def exitForStatExpr(self, ctx:SasParser.ForStatExprContext):
        pass


    # Enter a parse tree produced by SasParser#forSeq.
    def enterForSeq(self, ctx:SasParser.ForSeqContext):
        pass

    # Exit a parse tree produced by SasParser#forSeq.
    def exitForSeq(self, ctx:SasParser.ForSeqContext):
        pass


    # Enter a parse tree produced by SasParser#seq.
    def enterSeq(self, ctx:SasParser.SeqContext):
        pass

    # Exit a parse tree produced by SasParser#seq.
    def exitSeq(self, ctx:SasParser.SeqContext):
        pass


    # Enter a parse tree produced by SasParser#while_.
    def enterWhile_(self, ctx:SasParser.While_Context):
        pass

    # Exit a parse tree produced by SasParser#while_.
    def exitWhile_(self, ctx:SasParser.While_Context):
        pass



del SasParser