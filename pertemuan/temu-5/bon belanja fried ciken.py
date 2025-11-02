print('-------GEROBAK FRIED CHICKEN-------')
print('-----------------------------------')
print('Kode      Jenis Potong    Harga    ')
print('-----------------------------------')
print(' D        Dada            Rp. 2500 ')
print(' P        Paha            Rp. 2000 ')
print(' S        Sayap           Rp. 1500 ')
print('-----------------------------------')

harga = {'D': 2500, 'P': 2000, 'S': 1500}
jenis_potong = {'D': 'Dada', 'P': 'Paha', 'S': 'Sayap'}

banyak_jenis = int(input("Banyak Jenis : "))

data = []
for i in range (banyak_jenis):
    print(f'\nJenis ke - {i+1}')
    kode = input("Kode Potog (D / P / S) : ").upper()
    if kode not in harga:
        print("Kode Tidak Ada!")
        continue
    banyak_beli = int(input("Banyak Potong : "))
    jumlah_harga = harga[kode] * banyak_beli
    data.append((jenis_potong[kode], harga[kode], banyak_beli, jumlah_harga))

print('GEROBAK FRIED CHICKEN')
print('=======================================================')
print('No   Jenis Potong    Harga   Banyak  Jumlah Harga')
print('-------------------------------------------------------')

total = 0
for i, (jenis, hrg, banyak, Jumlah) in enumerate(data, start=1) :
    print(f"{i:<3} {jenis:<14} Rp{hrg:7}   {banyak:<7} Rp{Jumlah}")
    total += Jumlah

pajak = total * 0.10
total_bayar = total + pajak

print('-------------------------------------------------------')
print(f"Jumlah Bayar        : Rp {total}")
print(f"Pajak 10%           : Rp {int(pajak)}")
print(f"Total Bayar         : Rp {int(total_bayar)}")
print('=======================================================')
