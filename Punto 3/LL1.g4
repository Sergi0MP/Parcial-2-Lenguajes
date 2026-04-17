grammar LL1;

program: s EOF;

s: aRule A aRule B
 | bRule B bRule A
 ;

aRule: ; // ε
bRule: ; // ε

A: 'a';
B: 'b';

WS: [ \t\r\n]+ -> skip;
