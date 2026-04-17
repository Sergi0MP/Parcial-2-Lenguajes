import time

# Gramática en CNF
grammar = {
    "E": [("E", "PLUS"), ("E", "TIMES"), ("LPAREN", "X"), ("n",)],
    "PLUS": [("+", "E")],
    "TIMES": [("*", "E")],
    "X": [("E", "RPAREN")],
}

def cyk_parse(tokens):
    n = len(tokens)
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Llenar diagonal
    for i in range(n):
        for lhs, rules in grammar.items():
            for rule in rules:
                if len(rule) == 1 and rule[0] == tokens[i]:
                    table[i][i].add(lhs)

    # Llenar tabla
    for l in range(2, n + 1):  # longitud
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for lhs, rules in grammar.items():
                    for rule in rules:
                        if len(rule) == 2:
                            B, C = rule
                            if B in table[i][k] and C in table[k+1][j]:
                                table[i][j].add(lhs)

    return "E" in table[0][n-1]

def tokenize(expr):
    tokens = []
    for c in expr:
        if c.isdigit():
            tokens.append("n")
        elif c in "+*()":
            tokens.append(c)
    return tokens

def main():
    with open("pruebas.txt", "r") as file:
        for line in file:
            expr = line.strip()
            if not expr:
                continue

            tokens = tokenize(expr)

            start = time.time()
            result = cyk_parse(tokens)
            end = time.time()

            print(f"\nExpresión: {expr}")
            if result:
                print("Resultado: válida")
            else:
                print("Resultado: inválida")

            print(f"Tiempo CYK: {end - start:.6f} segundos")

if __name__ == "__main__":
    main()
