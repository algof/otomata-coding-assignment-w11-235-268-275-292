# Tugas Minggu ke-11 Otomata
| Name           | NRP        | Kelas     | Kelompok    |
| ---            | ---        | ----------| ---         |
| Algof Kristian Zega | 5025231235 | Otomata (E) | Kelompok 5 |
| Gregorius Setiadharma | 5025231268 | Otomata (E) | Kelompok 5 |
| Muhammad Davin Aulia Risky | 5025231275 | Otomata (E) | Kelompok 5 |
| Muhammad Aditya Handrian | 5025231292 | Otomata (E) | Kelompok 5 |

---

### Penjelasan mengenai CYK algorithm dan cara kerjanya

```import json

def cykParse(grammar):
    non_terminals = grammar["non_terminals"]
    terminals = grammar["terminals"]
    rules = grammar["production_rules"]
    start_symbol = grammar["start_symbol"]
    w = grammar["sentence"]
    
    n = len(w) # n = banyak elemen dalam string w
    
    # Inisialisasi tabel CYK sebanyak n kali n
    T = [[set() for _ in range(n)] for _ in range(n)]```

Kode di atas mengekstrak komponen grammar dari parameter masukan dan membuat tabel CYK (matriks T) berukuran n×n, di mana n adalah panjang kalimat yang akan diparsing. Setiap sel T[i][j] adalah himpunan (set) yang akan berisi simbol non-terminal yang dapat menghasilkan substring dari posisi i hingga j

   ```# Basis: isian diagonal (produksi langsung dari terminal)
    for j in range(n):
        for lhs, rule_list in rules.items():
            for rhs in rule_list:
                if len(rhs) == 1 and rhs[0] == w[j]:
                    T[j][j].add(lhs)```

Bagian ini mengisi elemen diagonal tabel (T[j][j]) dengan simbol non-terminal yang dapat langsung menghasilkan terminal pada posisi j dalam kalimat. Ini sesuai dengan langkah pertama algoritma CYK standard, tetapi menggunakan indeks berbasis

       ```# Aturan produksi untuk span yang lebih panjang
        for i in range(j, -1, -1):
            for k in range(i, j):
                for lhs, rule_list in rules.items():
                    for rhs in rule_list:
                        if len(rhs) == 2:
                            B, C = rhs
                            if B in T[i][k] and C in T[k + 1][j]:
                                T[i][j].add(lhs)```

Bagian ini adalah inti dari algoritma CYK. Untuk setiap substring w[i...j], kode memeriksa apakah ada aturan produksi A → BC di mana B dapat menghasilkan substring w[i...k] dan C dapat menghasilkan substring w[k+1...j]. Jika ada, maka A ditambahkan ke sel T[i][j]

```# Apakah simbol awal dapat menghasilkan seluruh kalimat?
    if start_symbol in T[0][n - 1]:
        print("True")
    else:
        print("False")```

Bagian terakhir memeriksa apakah simbol awal (start_symbol) terdapat dalam sel T[n-1], yang merepresentasikan apakah simbol awal dapat menghasilkan seluruh kalimat. Jika ya, berarti kalimat dapat diterima oleh grammar

```# Load grammar dari file JSON
with open("input.json", "r") as f:
    grammar_data = json.load(f)

cykParse(grammar_data)```

---

### Cara menggunakan program

Buat file dengan nama `input.json` lalu sesuaikan isi file dengan format. File json berisi:
1. Non-terminal symbols or placeholder
2. Terminal symbols or final output symbols
3. Production rules to create symbols sequence
4. Start symbol (where to start producing sentences).

Contoh penulisannya dapat dilihat di bagian sample input dan sample output.

Jalankan file.

---

### Sample input dan sample output

Output `True` bila Grammar yang ada dapat membentuk string yang dicek.

Output `False` bila Grammar yang ada tidak dapat membentuk string yang dicek.

Input 1 :

`input.json`

```json
{
  "non_terminals": ["NP", "Nom", "Det", "AP", "Adv", "A"],
  "terminals": ["book", "orange", "man", "tall", "heavy", "very", "muscular"],
  "production_rules": {
    "NP": [["Det", "Nom"]],
    "Nom": [["AP", "Nom"], ["book"], ["orange"], ["man"]],
    "AP": [["Adv", "A"], ["heavy"], ["orange"], ["tall"]],
    "Det": [["a"]],
    "Adv": [["very"], ["extremely"]],
    "A": [["heavy"], ["orange"], ["tall"], ["muscular"]]
  },
  "start_symbol": "NP",
  "sentence": ["a", "very", "heavy", "orange", "book"]
}
```

Output 1 : 

```txt
True
```

Input 2 :

`input_2.json`

```json
{
  "non_terminals": ["S", "A", "B", "C", "D", "E", "F"],
  "terminals": ["a", "b", "c"],
  "production_rules": {
    "S": [["A", "B"]],
    "A": [["C", "D"], ["C", "F"]],
    "B": [["c"], ["E", "B"]],
    "C": [["a"]],
    "D": [["b"]],
    "E": [["c"]],
    "F": [["A", "D"]]
  },
  "start_symbol": "S",
  "sentence": ["a", "a", "a", "b", "b", "b", "c", "c"]
}
```

Output 2 :

```txt
True
```
