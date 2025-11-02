kode_baju = input("masukan kode baju [SP/AD] : ")
ukuran = input("masukan ukuran baju [S/M] : ")

if kode_baju == "SP" or kode_baju == "sp" :
    merk = "SuperDry"
    if ukuran == "S" or ukuran == "s" :
        harga = 450000
    elif ukuran == "M" or ukuran == "m" :
        harga = 500000
    else :
        harga = 0
elif kode_baju == "AD" or kode_baju == "ad" :
    merk = "Adidas"
    if ukuran == "S" or ukuran == "s" :
        harga = 450000
    elif ukuran == "M" or ukuran == "m" :
        harga = 500000
    else :
        harga = 0
else:
    merk = "anda salah input kode merk"
    harga = 0

print("=========================")
print("Merk Baju : "+str(merk))
print(f"Harga Baju : Rp {harga:,.0f}")