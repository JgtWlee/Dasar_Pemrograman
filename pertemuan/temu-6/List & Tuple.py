

a = [1, 2, 3, 4, 5]

a.append(6) #tambah 1
a.extend([7, 8, 9]) #tambah banyak
a[0] = 10 #ubah index 0
a.remove(4) #hapus 4
a.pop(1) #hapus index 1

a.insert(2,100) #menyisipkan angka

print(a)

b = ['a','c','b','d']

print(sorted(b)) #urut asscending
b.sort() #mengurutkan alfabet dan nomor
print(b)

print(sorted(b, reverse=True)) #urut descending
b.sort(reverse=True) #mengurutkan terbalik
print(b)