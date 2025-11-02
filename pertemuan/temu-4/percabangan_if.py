'''Nilai = int(input('Masukan Nilai anda : '))
if Nilai >= 70:
    print('Selamat anda Lulus Ujian')
else:
    print('Dongo')
'''

gaji_pokok = 5000000

jumlah_produk = int(input('Masukan jumlah produk terjual :'))
harga_satuan = int(input('Masukan harga satuan produk :'))

omset = jumlah_produk * harga_satuan

if jumlah_produk >= 100:
    bonus = 0.20 * omset
else:
    bonus = 0.10 * omset

total_gaji = gaji_pokok + bonus

print("============================")
print("jumlah produk terjual   : ", jumlah_produk)
print("harga satuan produk     : ", harga_satuan)
print("omset penjualan         : ", omset)
print("bonus penjualan         : ", bonus)
print(" total gaji diterima    : ", total_gaji)



