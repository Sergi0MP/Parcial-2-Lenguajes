%{
#include "calculadora.tab.h"
%}

%%

"true"     { return TRUE; }
"false"    { return FALSE; }

"&&"       { return AND; }
"||"       { return OR; }
"!"        { return NOT; }

"("        { return LPAREN; }
")"        { return RPAREN; }

[ \t\n]    ;  // ignorar espacios

.          { return yytext[0]; }

%%
int yywrap() {
    return 1;
}
