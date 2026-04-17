grammar CRUD;

// Regla inicial
program: instruccion+ EOF;

// Instrucciones
instruccion
    : crear
    | leer
    | actualizar
    | borrar
    ;

// Operaciones CRUD
crear: INSERT INTO ID VALUES objeto;

leer: FIND IN ID WHERE filtro;

actualizar: UPDATE ID SET objeto WHERE filtro;

borrar: REMOVE FROM ID WHERE filtro;

// Objeto tipo JSON
objeto
    : LBRACE listaAtributos RBRACE
    | LBRACE RBRACE
    ;

listaAtributos
    : par
    | listaAtributos COMA par
    ;

par: ID DOSPUNTOS valor;

// Valores
valor
    : STRING
    | NUMBER
    | BOOLEAN
    ;

// Expresiones (precedencia)
filtro
    : filtro OR terminoAnd
    | terminoAnd
    ;

terminoAnd
    : terminoAnd AND comparacion
    | comparacion
    ;

comparacion
    : ID OP_REL valor
    ;

// TOKENS
INSERT: 'INSERT';
INTO: 'INTO';
VALUES: 'VALUES';
FIND: 'FIND';
IN: 'IN';
WHERE: 'WHERE';
UPDATE: 'UPDATE';
SET: 'SET';
REMOVE: 'REMOVE';
FROM: 'FROM';

OR: '||';
AND: '&&';

OP_REL: '==' | '!=' | '>' | '<' | '>=' | '<=';

BOOLEAN: 'true' | 'false';

ID: [a-zA-Z_][a-zA-Z0-9_]*;

NUMBER: [0-9]+ ('.' [0-9]+)?;

STRING: '"' .*? '"' | '\'' .*? '\'';

LBRACE: '{';
RBRACE: '}';
COMA: ',';
DOSPUNTOS: ':';

WS: [ \t\r\n]+ -> skip;
