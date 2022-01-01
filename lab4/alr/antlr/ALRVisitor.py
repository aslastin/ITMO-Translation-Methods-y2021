# Generated from ALR.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ALRParser import ALRParser
else:
    from ALRParser import ALRParser

# This class defines a complete generic visitor for a parse tree produced by ALRParser.

class ALRVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ALRParser#start.
    def visitStart(self, ctx:ALRParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#DescRule.
    def visitDescRule(self, ctx:ALRParser.DescRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#DescTerminal.
    def visitDescTerminal(self, ctx:ALRParser.DescTerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#DescSkip.
    def visitDescSkip(self, ctx:ALRParser.DescSkipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#rights.
    def visitRights(self, ctx:ALRParser.RightsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#RightMember.
    def visitRightMember(self, ctx:ALRParser.RightMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#RightEps.
    def visitRightEps(self, ctx:ALRParser.RightEpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#MemberNterminal.
    def visitMemberNterminal(self, ctx:ALRParser.MemberNterminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#MemberTerminal.
    def visitMemberTerminal(self, ctx:ALRParser.MemberTerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#MemberRegexp.
    def visitMemberRegexp(self, ctx:ALRParser.MemberRegexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#MemberFunc.
    def visitMemberFunc(self, ctx:ALRParser.MemberFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#eps.
    def visitEps(self, ctx:ALRParser.EpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#nterminal.
    def visitNterminal(self, ctx:ALRParser.NterminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#terminal.
    def visitTerminal(self, ctx:ALRParser.TerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#regexp.
    def visitRegexp(self, ctx:ALRParser.RegexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#func.
    def visitFunc(self, ctx:ALRParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ALRParser#skip.
    def visitSkip(self, ctx:ALRParser.SkipContext):
        return self.visitChildren(ctx)



del ALRParser