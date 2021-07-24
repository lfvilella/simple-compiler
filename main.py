import simple_lexer
import simple_parser


def main():
    lexer = simple_lexer.SimpleLexer('$x = 200 + 200; print($x);')
    parser = simple_parser.SimpleParser(lexer)
    print(parser.prog())


if __name__ == '__main__':
    main()
