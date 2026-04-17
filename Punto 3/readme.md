# Punto 3 - Demostración LL(1)

## Descripción

Se implementó la gramática del ejercicio utilizando ANTLR y Python para demostrar que es LL(1).

---

## Archivos

* LL1.g4: gramática implementada
* test_ll1.py: programa de prueba
* pruebas.txt: entradas de prueba
* evidencia_LL1.txt: explicación teórica

---

## Ejecución

1. Generar parser:

antlr4 -Dlanguage=Python3 LL1.g4

2. Ejecutar:

python test_ll1.py

---

## Resultado

El parser acepta las entradas válidas (ab, ba) sin ambigüedad.

---

## Conclusión

No existen conflictos de predicción y la gramática puede analizarse con un solo símbolo de anticipación, por lo tanto es LL(1).
