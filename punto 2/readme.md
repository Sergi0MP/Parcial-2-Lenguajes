# Punto 2 - Implementación de Gramática CRUD con ANTLR

## Descripción

En este punto se implementa una gramática para un lenguaje CRUD (Create, Read, Update, Delete) orientado a bases de datos no relacionales, utilizando ANTLR y Python.

El sistema permite validar instrucciones como INSERT, FIND, UPDATE y REMOVE, generando su respectivo árbol sintáctico.

---

## Requisitos

* Python 3
* Java (JDK 11 o superior)
* ANTLR 4
* Librería: antlr4-python3-runtime

---

## Instalación

1. Instalar dependencias:

```
sudo apt update
sudo apt install openjdk-11-jdk python3 python3-venv -y
```

2. Crear entorno virtual:

```
python3 -m venv venv
source venv/bin/activate
```

3. Instalar ANTLR runtime:

```
pip install antlr4-python3-runtime
```

---

## Generación del Analizador

Ejecutar el siguiente comando para generar el parser:

```
antlr4 -Dlanguage=Python3 CRUD.g4
```

---

## Ejecución

Ejecutar el programa:

```
python test.py
```

Luego ingresar una consulta cuando el sistema lo solicite.

---

## Ejemplos de entrada

```
INSERT INTO usuarios VALUES {nombre:"Juan", edad:25}

FIND IN ventas WHERE total > 100 || zona == "norte"

UPDATE usuarios SET {edad:30} WHERE nombre == "Juan"

REMOVE FROM usuarios WHERE edad < 18
```

---

## Resultado

El sistema valida la sintaxis de la consulta y muestra el árbol sintáctico correspondiente.

Si la entrada es incorrecta, se reporta un error sintáctico.

---

## Notas

* La gramática implementa precedencia de operadores en la cláusula WHERE.
* Se utilizaron estructuras tipo JSON para representar objetos.
* El analizador fue generado automáticamente con ANTLR.
