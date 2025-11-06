tabel = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for baris in range(len(tabel)):
    for kolom in range(len(tabel[baris])):
        print(f"baris {baris+1}, kolom {kolom+1} adalah : {tabel[baris][kolom]}")  