# Diseño de Gramática para Lenguaje CRUD en Base de Datos No Relacional

---

## 1.1 Definición de la Gramática Independiente del Contexto (GIC)

Se define una gramática que permite representar operaciones de tipo CRUD (**Create, Read, Update, Delete**) sobre una base de datos no relacional, utilizando una sintaxis inspirada en consultas tipo documento.

### Tabla de No Terminales y Producciones

| No Terminal      | Reglas de Producción                              | Descripción                              |
|------------------|---------------------------------------------------|------------------------------------------|
| `program`        | `program → instruccion+`                          | Símbolo inicial. Permite múltiples instrucciones |
| `instruccion`    | `instruccion → crear \| leer \| actualizar \| borrar` | Define el conjunto de operaciones CRUD   |
| `crear`          | `crear → INSERT INTO ID VALUES objeto`            | Inserción de un documento                |
| `leer`           | `leer → FIND IN ID WHERE filtro`                  | Consulta con condición                   |
| `actualizar`     | `actualizar → UPDATE ID SET objeto WHERE filtro`  | Modificación de documentos               |
| `borrar`         | `borrar → REMOVE FROM ID WHERE filtro`            | Eliminación de documentos                |
| `objeto`         | `objeto → { listaAtributos } \| { }`              | Representación de estructura tipo JSON   |
| `listaAtributos` | `listaAtributos → par \| listaAtributos , par`    | Lista de atributos                       |
| `par`            | `par → ID : valor`                                | Asociación clave-valor                   |
| `valor`          | `valor → STRING \| NUMBER \| BOOLEAN`             | Tipos de datos soportados                |

---

## 1.2 Jerarquía de Precedencia y Asociatividad de Expresiones

Para evitar ambigüedades en la evaluación de expresiones dentro de la cláusula `WHERE`, se define una jerarquía de operadores utilizando diferentes no terminales.

### Tabla de Precedencia

| Nivel | Operador                        | No Terminal   | Asociatividad | Precedencia |
|-------|---------------------------------|---------------|---------------|-------------|
| 1     | `\|\|` (OR)                     | `filtro`      | Izquierda     | Baja        |
| 2     | `&&` (AND)                      | `terminoAnd`  | Izquierda     | Media       |
| 3     | `==, !=, >, <, >=, <=`          | `comparacion` | No aplica     | Alta        |

### Reglas de Producción para Expresiones

```
filtro → filtro || terminoAnd
       | terminoAnd

terminoAnd → terminoAnd && comparacion
           | comparacion

comparacion → ID OP_REL valor
```

---

## 1.3 Estructura de Datos y Manejo de Listas

La gramática permite manejar listas de atributos mediante **recursión por la izquierda**, lo cual facilita la construcción de estructuras tipo JSON.

### Reglas de Producción

```
objeto → { listaAtributos }
       | { }

listaAtributos → par
               | listaAtributos , par

par → ID : valor
```

### Ejemplo de Derivación

**Entrada:**
```
ID : valor , ID : valor
```

**Proceso de reducción (analizador ascendente):**
```
par , ID : valor
par , par
listaAtributos
```

Esto permite manejar listas de longitud arbitraria de manera eficiente.

---

## 1.4 Gramática Completa

```
program → instruccion+

instruccion → crear
            | leer
            | actualizar
            | borrar

crear → INSERT INTO ID VALUES objeto
leer  → FIND IN ID WHERE filtro
actualizar → UPDATE ID SET objeto WHERE filtro
borrar → REMOVE FROM ID WHERE filtro

objeto → { listaAtributos }
       | { }

listaAtributos → par
               | listaAtributos , par

par → ID : valor

valor → STRING
      | NUMBER
      | BOOLEAN

filtro → filtro || terminoAnd
       | terminoAnd

terminoAnd → terminoAnd && comparacion
           | comparacion

comparacion → ID OP_REL valor
```

---

## 1.5 Especificación de Tokens (Análisis Léxico)

Se definen los tokens necesarios para el análisis léxico del lenguaje.

### Tabla de Tokens

| Token               | Expresión Regular / Valor                                        | Descripción                      |
|---------------------|------------------------------------------------------------------|----------------------------------|
| Palabras reservadas | `INSERT, FIND, UPDATE, REMOVE, INTO, VALUES, WHERE, SET`        | Palabras clave del lenguaje      |
| `ID`                | `[a-zA-Z_][a-zA-Z0-9_]*`                                        | Identificadores                  |
| `STRING`            | `".?"` \| `'.?'`                                                 | Cadenas de texto                 |
| `NUMBER`            | `[0-9]+(\.[0-9]+)?`                                              | Números enteros o decimales      |
| `BOOLEAN`           | `true \| false`                                                  | Valores booleanos                |
| `OP_REL`            | `== \| != \| > \| < \| >= \| <=`                                | Operadores relacionales          |
| `WS`                | `[ \t\r\n]+ → skip`                                             | Espacios en blanco ignorados     |

---

## 1.6 Propiedades de la Gramática

- La gramática es **independiente del contexto (GIC)**.
- Presenta **recursividad por la izquierda**, adecuada para analizadores tipo LALR.
- Define explícitamente la **precedencia de operadores**, evitando ambigüedades.
- Permite la **construcción de estructuras dinámicas** mediante listas recursivas.
- Es adecuada para implementación en herramientas como **ANTLR**.
