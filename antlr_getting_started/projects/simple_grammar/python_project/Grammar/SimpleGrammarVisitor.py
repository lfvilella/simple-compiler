# Generated from /Users/felipe/projects/simple-compiler/antlr_getting_started/projects/simple_grammar/SimpleGrammar.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleGrammarParser import SimpleGrammarParser
else:
    from SimpleGrammarParser import SimpleGrammarParser

# This class defines a complete generic visitor for a parse tree produced by SimpleGrammarParser.

class SimpleGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleGrammarParser#prog.
    def visitProg(self, ctx:SimpleGrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleGrammarParser#expr.
    def visitExpr(self, ctx:SimpleGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleGrammarParser#term.
    def visitTerm(self, ctx:SimpleGrammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleGrammarParser#fact.
    def visitFact(self, ctx:SimpleGrammarParser.FactContext):
        return self.visitChildren(ctx)



del SimpleGrammarParser