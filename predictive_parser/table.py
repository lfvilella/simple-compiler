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
 	|    id    |     +      |     *	     |     (    |    )    |     $   |  # noqa: W191, E101, E501
----+----------+------------+------------+----------+---------+---------|
E	| E –> TE’ |   error 	|    error   | E –> TE’ |	sync  |   sync  |
----+----------+------------+------------+----------+---------+---------|
E’	|   error  | E’ –> +TE’ |    error   | 	 error	| E’ –> ε |	E’ –> ε |
----+----------+------------+------------+----------+---------+---------|
T	| T –> FT’ |	sync	|    error   | T –> FT’ |	sync  |   sync  |
----+----------+------------+------------+----------+---------+---------|
T’	|   error  |  T’ –> ε	| T’ –> *FT’ |	 error  | T’ –> ε |	T’ –> ε |
----+----------+------------+------------+----------+---------+---------|
F	| F –> id  | 	 sync   |     sync   | F –> (E) |   sync  |  sync   |
"""

START_SYMBOL = 'E'
EMPTY = 'empty'  # ε
EOF = '$'

FATAL_ERROR = 'fatal_error'
SYNC_ERROR = 'sync'

PARSING_TABLE = {
    START_SYMBOL: {
        'id': "TE'",
        '+': FATAL_ERROR,
        '*': FATAL_ERROR,
        '(': "TE'",
        ')': SYNC_ERROR,
        EOF: SYNC_ERROR,
    },
    "E'": {
        'id': FATAL_ERROR,
        '+': "+TE'",
        '*': FATAL_ERROR,
        '(': FATAL_ERROR,
        ')': EMPTY,
        EOF: EMPTY,
    },
    'T': {
        'id': "FT'",
        '+': SYNC_ERROR,
        '*': FATAL_ERROR,
        '(': "FT'",
        ')': SYNC_ERROR,
        EOF: SYNC_ERROR,
    },
    "T'": {
        'id': FATAL_ERROR,
        '+': EMPTY,
        '*': "*FT'",
        '(': FATAL_ERROR,
        ')': EMPTY,
        EOF: EMPTY,
    },
    'F': {
        'id': 'id',
        '+': SYNC_ERROR,
        '*': SYNC_ERROR,
        '(': '(E)',
        ')': SYNC_ERROR,
        EOF: SYNC_ERROR,
    },
}


TERMINAL = set(['id', '+', '*', '(', ')'])
NONTERMINAL = set(PARSING_TABLE.keys())
