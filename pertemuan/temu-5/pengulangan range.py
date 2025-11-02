# Output: range(0,10)
print(range(10))

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]
print(list(range(10)))

# Output: [2, 3, 4, 5, 6, 7]
print(list(range(2, 8)))

# Output: [2, 5, 8, 11, 14, 17]
print(list(range(2, 20, 3)))

# Output: [3, 6, 9, 12]
print(list(range(3, 15, 3)))

# Program untuk iterasi list menggunakan pengindeksam

mapel = ['matematika', 'fisika', 'kimia']

for i in range(len(mapel)):
    print("saya suka", mapel[i])