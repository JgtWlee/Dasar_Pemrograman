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
c=input("Masukkan operator (+,-,x,:,**): "  )

if c=="+":
    operator='tambah'
    total=hitung(a,b)   
elif c=="-":
    operator='kurang'
    total=kurang(a,b)   
elif c=="x":
    operator='kali'
    total=kali(a,b)
elif c==":":
    operator='bagi'
    total=bagi(a,b)
elif c=="**":
    operator='pangkat'
    total=pangkat(a,b)
else:
    total="operator tidak ditemukan"

print(f"hasil {operator} {a} dengan {b} : {total}")