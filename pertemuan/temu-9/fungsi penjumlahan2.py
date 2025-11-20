def hitung (a,b):
    total=a+b
    return total

def kurang (a,b):
    total=a-b
    return total

def kali (a,b):
    total=a*b
    return total

def bagi (a,b):
    total=a/b
    return total  

def pangkat (a,b):
    total=a**b
    return total  

print("Program Kalkulator python Sederhana")
a=int(input("Masukkan angka pertama: "  ))
b=int(input("Masukkan angka kedua: "  ))
c=input("Masukkan operator (tambah,kurang,kali,bagi,pangkat,semuanya)): "  ).lower()


if c=="tambah":
    print(f"Hasil tambah {a} dengan {b} : {hitung(a,b)}")
elif c=="kurang":
    print(f"Hasil kurang {a} dengan {b} : {kurang(a,b)}")
elif c=="kali":
    print(f"Hasil kali {a} dengan {b} : {kali(a,b)}")  
elif c=="bagi": 
    print(f"Hasil bagi {a} dengan {b} : {bagi(a,b)}") 
elif c=="pangkat":
    print(f"Hasil pangkat {a} dengan {b} : {pangkat(a,b)}")
elif c=="semuanya":  
    print(f"Hasil tambah {a} dengan {b} : {hitung(a,b)}")
    print(f"Hasil kurang {a} dengan {b} : {kurang(a,b)}")
    print(f"Hasil kali {a} dengan {b} : {kali(a,b)}")   
    print(f"Hasil bagi {a} dengan {b} : {bagi(a,b)}")  
    print(f"Hasil pangkat {a} dengan {b} : {pangkat(a,b)}")
else:
    print("operator tidak ditemukan")
