# simple-compiler
A simple compiler built on the UENP Compiler subject

# Example
```py
lexer = simple_lexer.SimpleLexer(
    '$x = (2 - 2) + 2/5;'
    '$y = 2 * 10 + 1;'
    '$z = ($x + $y) * 5;'
    '$p = 3.14 - $z;'
    'print($p);'
)
parser = simple_parser.SimpleParser(lexer)
parser.prog()

# stdout: -103.86
```

# Reference

*based from: [wellingtondellamura/compiler-from-scratch](https://github.com/wellingtondellamura/compiler-from-scratch/tree/master/)*
