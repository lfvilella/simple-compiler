"""Table

Grammar:
    E --> TE'
    E' --> +TE' | ε
    T --> FT'
    T' --> *FT' | ε
    F --> id | (E)

First/Follow:
Rule         |   First   |   Follow       |
-------------+-----------+----------------|
E –> TE’     | { id, ( } | { $, ) }       |
E’ –> +TE’/ε | { +, ε }  | { $, ) }       |
T –> FT’     | { id, ( } | { +, $, ) }    |
T’ –> *FT’/ε | { *, ε }  | { +, $, ) }    |
F –> id/(E)  | { id, ( } | { *, +, $, ) } |

Parsing Table:
 	|    id    |     +      |     *	     |     (    |    )    |     $   |
----+----------+------------+------------+----------+---------+---------|
E	| E –> TE’ |	 	 	|            | E –> TE’ |	 	  |         |
----+----------+------------+------------+----------+---------+---------|
E’	|          | E’ –> +TE’ |            | 	 	 	| E’ –> ε |	E’ –> ε |
----+----------+------------+------------+----------+---------+---------|
T	| T –> FT’ |	 	 	|            | T –> FT’ |	 	  |         |
----+----------+------------+------------+----------+---------+---------|
T’	|          |  T’ –> ε	| T’ –> *FT’ |	 	    | T’ –> ε |	T’ –> ε |
----+----------+------------+------------+----------+---------+---------|
F	| F –> id  | 	 	    |            | F –> (E) |         |         |
"""

START_SYMBOL = 'E'
EMPTY = 'empty'  # ε

PARSING_TABLE = {
    START_SYMBOL: {
        'id': "TE'",
        '+': None,
        '*': None,
        '(': "TE'",
        ')': None,
        '$': None,
    },
    "E'": {
        'id': None,
        '+': "+TE'",
        '*': None,
        '(': None,
        ')': EMPTY,
        '$': EMPTY,
    },
    'T': {
        'id': "FT'",
        '+': None,
        '*': None,
        '(': "FT'",
        ')': None,
        '$': None,
    },
    "T'": {
        'id': None,
        '+': EMPTY,
        '*': "*FT'",
        '(': None,
        ')': EMPTY,
        '$': EMPTY,
    },
    'F': {'id': 'id', '+': None, '*': None, '(': '(E)', ')': None, '$': None,},
}
