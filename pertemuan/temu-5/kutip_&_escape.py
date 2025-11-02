# Menggunakan kutip tiga
print('''He said, "What's there?"''')

# Menggunakan Karakter escape untuk tanda Kutip tunggal
print('He said, "what\'s there?"')

# Menggunakan karakter escape untuk tanda kutip ganda
print("He said, \"what's there?\"")




print("ini adalah \x48\x45\x58 \ngood")


# Menggunakan posisi default
default_order = "{}, {} dan {}". format("Budi", "Galih", "Ratna")
print('\n--- Urutan default ---')
print(default_order)

# Menggunakan argument posisi
positional_order = "{1}, {0} dan {2}". format("Budi", "Galih", "Ratna")
print('\n--- Urutan berdasarkan posisi ---')
print(positional_order)


# Format Integer
print("{0} bila di ubah jadi biner menjadi {0:b}".format(12))

# Format Eksponensial
print("Fromat eksponensial: {0:e}".format(1566.345))

# Format Float
print("Sepertiga sama dengan : {0:3f}".format(1/3))

# Meratakan String
print("|{:<10}|{:^10}|{:>10}".format('beras', 'gula', 'garam'))



print("=================================================")
print("Universitas Bina Sarana Informatika". lower())
print("Universitas Bina Sarana Informatika". upper())
print("I love programming in Python".split())
print("I love Python".startswith("I"))
print("Saya belajar python".endswith("on"))
print(' - '.join((['I', 'love', 'you'])))
print("Belajar Java di BSI".replace('Java', 'Python'))