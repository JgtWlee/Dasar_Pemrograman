gaji_pokok = 300000

nama = input("Masukan Nama Anda : ")
golongan = int(input("Masukan Golongan Anda (1/2/3) : "))
pendidikan = input("Masukan Pendidikan anda (SMA/D1/D3/S1) : ")
jam_kerja = int(input("Masukan Jumlah Jam Kerja Anda : "))


if golongan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif  golongan == 3:    
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0

#=================================================

if pendidikan == "SMA" or pendidikan == "sma":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1" or pendidikan == "d1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3" or pendidikan == "d3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "S1" or pendidikan == "s1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0

#================================================

if jam_kerja > 8:
    lembur = (jam_kerja - 8) * 3500
else:
    lembur = 0

total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + lembur

print("=====================================================")
print("Karyawan Yang Bernama ", nama)
print("Honor Yang Di terima---------------------------------")
print(f"     Tunjangan Jabatan      : Rp{tunjangan_jabatan:,.0f}")
print(f"     Tunjangan Pendidikan   : Rp{tunjangan_pendidikan:,.0f}")
print(f"     Honor Lembur           : Rp{lembur:,.0f}")
print("      ===============================================")
print(f"     Total Gaji             : Rp{total_gaji:,.0f}")