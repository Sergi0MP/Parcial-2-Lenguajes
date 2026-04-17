# Punto 5 - Calculadora Booleana con YACC

## Descripción

Se implementó una calculadora de escritorio utilizando YACC y LEX para evaluar expresiones booleanas.

El sistema permite evaluar operaciones lógicas como AND, OR y NOT.

---

## Archivos

* lexer.l: análisis léxico
* calculadora.y: análisis sintáctico

---

## Operadores soportados

* && (AND)
* || (OR)
* ! (NOT)

---

## Ejecución

1. Generar parser:

bison -d calculadora.y

2. Generar lexer:

flex lexer.l

3. Compilar:

gcc lex.yy.c calculadora.tab.c -o calculadora

4. Ejecutar:

./calculadora

---

## Ejemplos

Entrada:
true && false

Salida:
Resultado: false

---

## Desempeño

El analizador sintáctico funciona en tiempo lineal O(n), ya que procesa la entrada en una sola pasada.

---

## Conclusión

El uso de YACC permite construir analizadores eficientes y estructurados, adecuados para lenguajes formales como expresiones booleanas.
