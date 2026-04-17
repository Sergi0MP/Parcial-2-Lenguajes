import time

def parse_expr(expr):
    try:
        eval(expr)
        return True
    except:
        return False

def main():
    expr = input("Ingrese expresión: ")

    start = time.time()
    result = parse_expr(expr)
    end = time.time()

    if result:
        print("Expresión válida")
    else:
        print("Expresión inválida")

    print(f"Tiempo Predictivo: {end - start:.6f} segundos")

if __name__ == "__main__":
    main()
