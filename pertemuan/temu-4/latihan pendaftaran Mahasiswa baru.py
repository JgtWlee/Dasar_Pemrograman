print("======Pendaftaran Mahasiswa Baru======")
nis = input("Masukan NIS anda : ")
nama = input("Masukan Nama anda : ")
jurusan = input(" Masukan Kode Jurusan anda ( SI / SIA ): ")

if jurusan == "SI" or jurusan == "si" :
    harga = 2400000
    prodi = "SI - Sistem Informasi" 
elif jurusan == "SIA" or jurusan == "sia":
    harga = 2000000
    prodi = "SIA - Sistem Informasi Akuntansi"
else:
    harga = 0
    prodi = "tidak diketahui"

print("=========Data Mahasiswa Baru==========")
print('======================================')
print("NIS      :", nis)
print("Nama     :", nama)
print("Jurusan  :", prodi )
print(f"Harga    : Rp.  {harga:,.0f}")
print('======================================')