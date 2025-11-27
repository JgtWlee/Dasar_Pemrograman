from kalkulator import tambah

angka1 =int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))   


hasil = tambah(angka1, angka2)
nama   = "tambah"

print(f"{angka1} {nama} {angka2} = {hasil:,.0f}")