import simple_lexer
import simple_parser


def main():
    lexer = simple_lexer.SimpleLexer(
        '$x = (2 - 2) + 2/5;'
        '$y = 2 * 10 + 1;'
        '$z = ($x + $y) * 5;'
        '$p = 3.14 - $z;'
        'print($p);'
    )
    parser = simple_parser.SimpleParser(lexer)
    parser.prog()


if __name__ == '__main__':
    main()
