import json

def cykParse(grammar):
    non_terminals = grammar["non_terminals"]
    terminals = grammar["terminals"]
    rules = grammar["production_rules"]
    start_symbol = grammar["start_symbol"]
    w = grammar["sentence"]
    
    n = len(w)
    
    # Inisialisasi tabel CYK
    T = [[set() for _ in range(n)] for _ in range(n)]

    # Basis: isian diagonal (produksi langsung dari terminal)
    for j in range(n):
        for lhs, rule_list in rules.items():
            for rhs in rule_list:
                if len(rhs) == 1 and rhs[0] == w[j]:
                    T[j][j].add(lhs)

        # Aturan produksi untuk span yang lebih panjang
        for i in range(j, -1, -1):
            for k in range(i, j):
                for lhs, rule_list in rules.items():
                    for rhs in rule_list:
                        if len(rhs) == 2:
                            B, C = rhs
                            if B in T[i][k] and C in T[k + 1][j]:
                                T[i][j].add(lhs)

    # Apakah simbol awal dapat menghasilkan seluruh kalimat?
    if start_symbol in T[0][n - 1]:
        print("True")
    else:
        print("False")

# Load grammar dari file JSON
with open("input.json", "r") as f:
    grammar_data = json.load(f)

cykParse(grammar_data)