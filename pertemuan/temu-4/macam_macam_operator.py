a = 10
b = 5
c = a > b
print("C adalah : ", c)

if c is True :
    print("nilai a lebis besar dari nilai b")
else:
    print("nilai a tidak lebih besar dari nilai b")

if c is not True :
    print("nilai a tidak lebih besar dari nilai b")
else:
    print("nilai a lebis besar dari nilai b")

#operator keanggotaan

a = [5, 10, 1, 20, 100]

if 11 in a:
    print("11 ada di dalam a")
else:
    print("11 tidak ada didalam a")