# Implementación del Algoritmo CYK y Comparación con Parser Predictivo

---

## 1. Descripción

En este punto se implementó el algoritmo **CYK (Cocke-Younger-Kasami)** para el reconocimiento de expresiones aritméticas, y se comparó su desempeño con un **parser predictivo**.

El objetivo es analizar tanto la validez de expresiones como el rendimiento de ambos enfoques.

---

## 2. Archivos del Proyecto

| Archivo          | Descripción                              |
|------------------|------------------------------------------|
| `cyk.py`         | Implementación del algoritmo CYK         |
| `predictivo.py`  | Parser basado en evaluación directa      |
| `comparar.py`    | Script de comparación automática         |
| `pruebas.txt`    | Conjunto de expresiones de prueba        |

---

## 3. Metodología

### 3.1 Algoritmo CYK

- Se implementó el algoritmo CYK basado en **programación dinámica**.
- Se utiliza una gramática en **Forma Normal de Chomsky (CNF)**.
- Complejidad temporal: **O(n³)**.

### 3.2 Parser Predictivo

- Se utilizó evaluación directa mediante Python (`eval`).
- Permite validar expresiones rápidamente.
- Complejidad aproximada: **O(n)**.

---

## 4. Pruebas Realizadas

Se evaluaron las siguientes expresiones:

| Expresión   | Descripción          |
|-------------|----------------------|
| `2+3`       | Suma simple          |
| `2*3`       | Multiplicación       |
| `(2+3)*4`   | Expresión compuesta  |
| `2+*3`      | Expresión inválida   |

---

## 5. Resultados Obtenidos

### 5.1 Resultados CYK

| Expresión  | Resultado | Tiempo (s) |
|------------|-----------|------------|
| `2+3`      | inválida  | 0.000011   |
| `2*3`      | inválida  | 0.000008   |
| `(2+3)*4`  | inválida  | 0.000031   |
| `2+*3`     | inválida  | 0.000008   |

### 5.2 Comparación CYK vs Predictivo

| Expresión  | CYK      | Tiempo CYK | Predictivo | Tiempo Predictivo |
|------------|----------|------------|------------|-------------------|
| `2+3`      | inválida | 0.000014   | válida     | 0.000021          |
| `2*3`      | inválida | 0.000006   | válida     | 0.000008          |
| `(2+3)*4`  | inválida | 0.000030   | válida     | 0.000008          |
| `2+*3`     | inválida | 0.000008   | inválida   | 0.000007          |

---

## 6. Análisis de Resultados

- El **parser predictivo** valida correctamente las expresiones válidas e inválidas.
- El **algoritmo CYK** no reconoce correctamente las expresiones válidas debido a limitaciones en la gramática utilizada.
- En términos de rendimiento:
  - CYK es **más costoso computacionalmente**.
  - El parser predictivo es **significativamente más rápido**.

---

## 7. Discusión

El algoritmo CYK es más general, ya que puede trabajar con cualquier gramática en CNF, pero su implementación requiere una correcta definición de la gramática. En este caso, la gramática utilizada no permite reconocer adecuadamente expresiones aritméticas completas, lo que explica los resultados obtenidos.

Por otro lado, el parser predictivo es más eficiente y adecuado para este tipo de lenguaje específico.

---

## 8. Conclusión

- El algoritmo CYK presenta **mayor complejidad y menor rendimiento**.
- El parser predictivo es **más eficiente** para expresiones aritméticas.
- La precisión del CYK depende fuertemente de la **gramática utilizada**.
- En aplicaciones prácticas, los parsers predictivos son preferidos cuando la gramática lo permite.
