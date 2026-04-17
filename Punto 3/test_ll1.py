from antlr4 import *
from LL1Lexer import LL1Lexer
from LL1Parser import LL1Parser

def parse_line(line):
    input_stream = InputStream(line)
    lexer = LL1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LL1Parser(stream)

    try:
        tree = parser.program()
        print(f"Entrada válida: {line.strip()}")
        print(tree.toStringTree(recog=parser))
    except:
        print(f"Entrada inválida: {line.strip()}")

def main():
    with open("pruebas.txt", "r") as file:
        for line in file:
            if line.strip():  # evitar líneas vacías
                parse_line(line)

if __name__ == "__main__":
    main()
