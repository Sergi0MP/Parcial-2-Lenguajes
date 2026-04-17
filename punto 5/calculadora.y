%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
%}

%token TRUE FALSE AND OR NOT LPAREN RPAREN

%left OR
%left AND
%right NOT

%%

input:
    expr { printf("Resultado: %s\n", $1 ? "true" : "false"); }
    ;

expr:
      expr AND expr   { $$ = $1 && $3; }
    | expr OR expr    { $$ = $1 || $3; }
    | NOT expr        { $$ = !$2; }
    | LPAREN expr RPAREN { $$ = $2; }
    | TRUE            { $$ = 1; }
    | FALSE           { $$ = 0; }
    ;

%%

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}

int main() {
    printf("Ingrese expresión booleana:\n");
    yyparse();
    return 0;
}
