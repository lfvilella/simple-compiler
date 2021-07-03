import simple_lexer
import simple_parser


def main():
    lexer = simple_lexer.SimpleLexer('2 + 4 / 2')
    parser = simple_parser.SimpleParser(lexer)
    print(parser.expression())


if __name__ == '__main__':
    main()
