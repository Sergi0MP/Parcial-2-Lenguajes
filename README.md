# Parcial 2 - Lenguajes de Programación

## Descripción General

En este proyecto se desarrollan e implementan diferentes técnicas de análisis sintáctico y diseño de lenguajes, abordando cinco puntos fundamentales:

1. Diseño de una gramática para operaciones CRUD.
2. Implementación de la gramática utilizando ANTLR.
3. Demostración de una gramática LL(1).
4. Implementación del algoritmo CYK y comparación con un parser predictivo.
5. Desarrollo de una calculadora booleana utilizando YACC.

---

## Estructura del Proyecto

```
Parcial_2/
│
├── Punto_1_Gramatica/
├── Punto_2_ANTLR/
├── Punto_3_LL1/
├── Punto_4_CYK/
└── Punto_5_YACC/
```

Cada carpeta contiene la solución independiente de cada punto, junto con su respectiva documentación.

---

## Requisitos Generales

* Sistema operativo: Linux (Ubuntu)
* Python 3
* Java (para ANTLR)
* ANTLR 4
* Bison y Flex (para YACC)

---

## Descripción de los Puntos

### Punto 1 - Diseño de Gramática

Se diseñó una gramática independiente del contexto para un lenguaje CRUD orientado a bases de datos no relacionales.

Se incluyeron:

* Reglas de producción
* Manejo de precedencia
* Definición de tokens
* Estructuras tipo JSON

---

### Punto 2 - Implementación con ANTLR

Se implementó la gramática en ANTLR y se generó un parser en Python.

Características:

* Validación de instrucciones CRUD
* Construcción de árboles sintácticos
* Manejo de expresiones con operadores lógicos

---

### Punto 3 - Demostración LL(1)

Se demostró que una gramática dada es LL(1) mediante:

* Cálculo de conjuntos FIRST
* Verificación de condiciones de no ambigüedad
* Implementación práctica en ANTLR
* Pruebas con cadenas válidas e inválidas

---

### Punto 4 - Algoritmo CYK

Se implementó el algoritmo CYK para validar expresiones aritméticas.

Además, se realizó una comparación con un parser predictivo:

* CYK: mayor complejidad (O(n³))
* Predictivo: mayor eficiencia (O(n))

Se analizaron tiempos de ejecución y comportamiento.

---

### Punto 5 - Calculadora con YACC

Se desarrolló una calculadora booleana utilizando Bison (YACC) y Flex.

Permite evaluar:

* AND (&&)
* OR (||)
* NOT (!)

Se resolvieron conflictos de precedencia mediante reglas de asociatividad.

---

## Ejecución General

Cada punto contiene su propio archivo README con instrucciones específicas para su ejecución.

---

## Conclusiones Generales

* Las gramáticas bien definidas permiten construir analizadores eficientes.
* Herramientas como ANTLR facilitan la generación de parsers automáticos.
* El algoritmo CYK es general pero menos eficiente que los parsers predictivos.
* YACC permite resolver ambigüedades mediante precedencia y asociatividad.
* La organización modular del proyecto facilita la comprensión y mantenimiento.

---

## Autor

Estudiante: Sergio Morales
Curso: Lenguajes de Programación
Periodo: 2026-1
