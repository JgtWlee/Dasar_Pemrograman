import kalkulator as kalk

angka1 =int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+, -, *, /, **, %): ")

if operator == '+':
    nama   = "tambah"
    hasil = kalk.tambah(angka1, angka2) 

elif operator == '-':
    nama   = "kurang"
    hasil = kalk.kurang(angka1, angka2)

elif operator == '*':
    nama   = "kali"
    hasil = kalk.kali(angka1, angka2)

elif operator == '/':
    nama   = "bagi"
    hasil = kalk.bagi(angka1, angka2)

elif operator == '**':
    nama   = "pangkat"
    hasil = kalk.pangkat(angka1, angka2)

elif operator == '%':
    nama   = "modulus"
    hasil = kalk.modulus(angka1, angka2)

else:
    hasil = "Operator tidak dikenali."

print(f"{angka1} {nama} {angka2} = {hasil:,.0f}")
