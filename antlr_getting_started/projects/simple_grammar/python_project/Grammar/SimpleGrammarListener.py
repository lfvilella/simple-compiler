# Generated from /Users/felipe/projects/simple-compiler/antlr_getting_started/projects/simple_grammar/SimpleGrammar.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleGrammarParser import SimpleGrammarParser
else:
    from SimpleGrammarParser import SimpleGrammarParser

# This class defines a complete listener for a parse tree produced by SimpleGrammarParser.
class SimpleGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleGrammarParser#prog.
    def enterProg(self, ctx:SimpleGrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by SimpleGrammarParser#prog.
    def exitProg(self, ctx:SimpleGrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by SimpleGrammarParser#expr.
    def enterExpr(self, ctx:SimpleGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by SimpleGrammarParser#expr.
    def exitExpr(self, ctx:SimpleGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by SimpleGrammarParser#term.
    def enterTerm(self, ctx:SimpleGrammarParser.TermContext):
        pass

    # Exit a parse tree produced by SimpleGrammarParser#term.
    def exitTerm(self, ctx:SimpleGrammarParser.TermContext):
        pass


    # Enter a parse tree produced by SimpleGrammarParser#fact.
    def enterFact(self, ctx:SimpleGrammarParser.FactContext):
        pass

    # Exit a parse tree produced by SimpleGrammarParser#fact.
    def exitFact(self, ctx:SimpleGrammarParser.FactContext):
        pass



del SimpleGrammarParser