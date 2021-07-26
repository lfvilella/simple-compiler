import sys

from interpreter import simple_lexer, simple_parser


class TestInterpreter:
    def test_scenario_1(self):
        temp = sys.stdout
        sys.stdout = open('test_scenario_1.log', 'w')

        lexer = simple_lexer.SimpleLexer(
            '$x = (2 - 2) + 2/5;'
            '$y = 2 * 10 + 1;'
            '$z = ($x + $y) * 5;'
            '$p = 3.14 - $z;'
            'print($p);'
        )
        parser = simple_parser.SimpleParser(lexer)
        parser.prog()

        sys.stdout.close()
        sys.stdout = temp

        with open('test_scenario_1.log') as file:
            first_line = float(file.readline())

        assert first_line == -103.86

    def test_scenario_2(self):
        temp = sys.stdout
        sys.stdout = open('test_scenario_2.log', 'w')

        lexer = simple_lexer.SimpleLexer(
            '$x = 2 - 2 + 2/5;'
            '$y = 2 * 10 + 1;'
            '$z = ($x + $y) * 5;'
            '$p = 3.14 - $z;'
            'print($p);'
        )
        parser = simple_parser.SimpleParser(lexer)
        parser.prog()

        sys.stdout.close()
        sys.stdout = temp

        with open('test_scenario_2.log') as file:
            first_line = float(file.readline())

        assert first_line == -99.86
