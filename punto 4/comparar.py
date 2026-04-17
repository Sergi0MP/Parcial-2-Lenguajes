import time

# ------------------------
# CYK (igual que antes)
# ------------------------

grammar = {
    "E": [("E", "PLUS"), ("E", "TIMES"), ("LPAREN", "X"), ("n",)],
    "PLUS": [("+", "E")],
    "TIMES": [("*", "E")],
    "X": [("E", "RPAREN")],
}

def cyk_parse(tokens):
    n = len(tokens)
    if n == 0:
        return False

    table = [[set() for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for lhs, rules in grammar.items():
            for rule in rules:
                if len(rule) == 1 and rule[0] == tokens[i]:
                    table[i][i].add(lhs)

    for l in range(2, n + 1):
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

# ------------------------
# Predictivo (rápido)
# ------------------------

def predictivo_parse(expr):
    try:
        eval(expr)
        return True
    except:
        return False

# ------------------------
# Comparación
# ------------------------

def main():
    print("Comparación CYK vs Predictivo\n")

    with open("pruebas.txt", "r") as file:
        for line in file:
            expr = line.strip()
            if not expr:
                continue

            # CYK
            tokens = tokenize(expr)
            start_cyk = time.time()
            result_cyk = cyk_parse(tokens)
            end_cyk = time.time()

            # Predictivo
            start_pred = time.time()
            result_pred = predictivo_parse(expr)
            end_pred = time.time()

            # Resultados
            print(f"Expresión: {expr}")

            print(f"  CYK:        {'válida' if result_cyk else 'inválida'} "
                  f"({end_cyk - start_cyk:.6f}s)")

            print(f"  Predictivo: {'válida' if result_pred else 'inválida'} "
                  f"({end_pred - start_pred:.6f}s)")

            print("-" * 40)


if __name__ == "__main__":
    main()
