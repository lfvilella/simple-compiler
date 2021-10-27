grammar DecisionGrammar;

prog: IF OEX NUM CEX OBK NUM CBK prog | p_elseif;
p_elseif: ELSEIF OEX NUM CEX OBK NUM CBK p_elseif | p_else;
p_else: ELSE OBK NUM CBK;

IF: 'if';
ELSEIF: 'else if';
ELSE: 'else';
OBK: '{';
CBK: '}';
OEX: '(';
CEX: ')';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NUM: [0-9]+;
VAR: [a-zA-Z]+;
WS: [ \t\r\n]+ -> skip;
