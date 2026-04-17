from antlr4 import *
from CRUDLexer import CRUDLexer
from CRUDParser import CRUDParser

def main():
    # Leer entrada desde archivo o consola
    input_stream = InputStream(input("Ingrese una consulta: \n"))

    # Análisis léxico
    lexer = CRUDLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Análisis sintáctico
    parser = CRUDParser(stream)
    tree = parser.program()

    print("\nConsulta válida. Árbol sintáctico:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
