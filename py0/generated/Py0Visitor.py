# Generated from Py0.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Py0Parser import Py0Parser
else:
    from Py0Parser import Py0Parser

# This class defines a complete generic visitor for a parse tree produced by Py0Parser.

class Py0Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Py0Parser#program.
    def visitProgram(self, ctx:Py0Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Py0Parser#statement.
    def visitStatement(self, ctx:Py0Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Py0Parser#functionDecl.
    def visitFunctionDecl(self, ctx:Py0Parser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Py0Parser#ifStatement.
    def visitIfStatement(self, ctx:Py0Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Py0Parser#elseIfStatement.
    def visitElseIfStatement(self, ctx:Py0Parser.ElseIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Py0Parser#elseStatement.
    def visitElseStatement(self, ctx:Py0Parser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Py0Parser#forStatement.
    def visitForStatement(self, ctx:Py0Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Py0Parser#whileStatement.
    def visitWhileStatement(self, ctx:Py0Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Py0Parser#repeatStatement.
    def visitRepeatStatement(self, ctx:Py0Parser.RepeatStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Py0Parser#block.
    def visitBlock(self, ctx:Py0Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Py0Parser#simpleStatement.
    def visitSimpleStatement(self, ctx:Py0Parser.SimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Py0Parser#expr.
    def visitExpr(self, ctx:Py0Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Py0Parser#baseExpr.
    def visitBaseExpr(self, ctx:Py0Parser.BaseExprContext):
        return self.visitChildren(ctx)



del Py0Parser