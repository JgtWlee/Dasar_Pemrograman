tabel = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print("===========")
print("[1, 2, 3],")
print("[4, 5, 6],")
print("[7, 8, 9],")
print("[0]")
print("=========================")

#input angka yang dicari = 6
angka = int(input("Masukkan angka yang dicari: "))

text_angka = ["pertama", "kedua", "ketiga", "keempat"]

ditemukan = 0

for baris in range(len(tabel)):
    for kolom in range(len(tabel[baris])):
        if tabel[baris][kolom] == angka:
            print(f"angka {angka} ada di baris ke {text_angka[baris]} kolom ke {text_angka[kolom]}")
            ditemukan += 1
            break

if ditemukan == 0:
    print(f"angka {angka} tidak ditemukan")