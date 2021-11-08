import click
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from Grammar.SimpleGrammarLexer import SimpleGrammarLexer
from Grammar.SimpleGrammarParser import SimpleGrammarParser
from Grammar.SimpleGrammarListener import SimpleGrammarListener


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(
            f'Coé, erro na linha {line}:{column}. Simbolo nada ve esse: {offendingSymbol.text}'
        )


class MyGrammarListener(SimpleGrammarListener):
    def enterFact(self, ctx: SimpleGrammarParser.FactContext):
        print('In fact')

    def exitFact(self, ctx: SimpleGrammarParser.FactContext):
        print('Out fact')


@click.command()
@click.option('--filepath', type=str, required=True)
def main(filepath):
    input_stream = FileStream(filepath)
    lexer = SimpleGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleGrammarParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(listener=MyErrorListener())
    tree = parser.prog()
    # printer = MyGrammarListener()
    # walker = ParseTreeWalker()
    # walker.walk(printer, tree)


if __name__ == '__main__':
    main()
