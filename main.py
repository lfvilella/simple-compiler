import simple_lexer
import simple_parser


def main():
    lexer = simple_lexer.SimpleLexer(
        '200 + 200 - 500 + 100 - 200 - 400 - 200 + 1100'
    )
    parser = simple_parser.SimpleParser(lexer)
    print(parser.expression())


if __name__ == '__main__':
    main()
