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

a=int(input("Masukkan angka pertama: "  ))
b=int(input("Masukkan angka kedua: "  ))

print(f"Hasil tambah {a} dengan {b} : {hitung(a,b)}")
print(f"Hasil kurang {a} dengan {b} : {kurang(a,b)}")
print(f"Hasil kali {a} dengan {b} : {kali(a,b)}")   
print(f"Hasil bagi {a} dengan {b} : {bagi(a,b)}")   
