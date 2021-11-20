grammar SimpleGrammar;

prog: (expr EOL)+;

expr: term (ADD | SUB) expr | term;
term: fact (MUL | DIV | MOD) term | fact;
fact: VAR | NUM | OPEN expr CLOSE;

EOL: ';';
OPEN: '(';
CLOSE: ')';
MOD: '%';
DIV: '/';
MUL: '*';
SUB: '-';
ADD: '+';
NUM: [0-9]+;
VAR: [a-zA-Z]+;
COMMENTS: '#' [~\r\n]+ -> skip;
WS: [ \t\r\n]+ -> skip;
