"""
Contoh penggunaan List dan Tuple di Python

File ini berisi contoh-contoh dasar dan berguna untuk memahami
perbedaan antara list (mutable) dan tuple (immutable).

Jalankan file ini untuk melihat output contoh.
"""

def show_list_examples():
	print("--- Contoh List (mutable) ---")

	# Membuat list
	buah = ["apel", "pisang", "jeruk"]
	print("List awal:", buah)

	# Mengakses elemen (indexing)
	print("Elemen pertama:", buah[0])
	print("Elemen terakhir:", buah[-1])

	# Slicing
	print("Slicing [0:2]:", buah[0:2])

	# Menambah elemen
	buah.append("mangga")
	print("Setelah append('mangga'):", buah)

	# Menyisipkan elemen di indeks tertentu
	buah.insert(1, "stroberi")
	print("Setelah insert(1, 'stroberi'):", buah)

	# Menghapus elemen
	buah.remove("pisang")
	print("Setelah remove('pisang'):", buah)

	# Pop (mengambil dan menghapus elemen terakhir)
	last = buah.pop()
	print("pop() mengembalikan:", last, "-> sisa list:", buah)

	# Mengubah elemen
	buah[0] = "apel merah"
	print("Setelah mengganti indeks 0:", buah)

	# Mengurutkan list (menggunakan copy untuk menjaga list asli bila ingin)
	angka = [3, 1, 4, 2]
	print("List angka sebelum sort():", angka)
	angka.sort()
	print("Setelah sort():", angka)

	# List comprehension
	kuadrat = [x * x for x in range(6)]
	print("List comprehension (kuadrat 0..5):", kuadrat)

	# Nested list
	matriks = [[1, 2], [3, 4], [5, 6]]
	print("Nested list (matriks):", matriks)

	# List adalah mutable: contoh perubahan di dalam nested list
	matriks[0][0] = 99
	print("Setelah ubah matriks[0][0] = 99 ->", matriks)


def show_tuple_examples():
	print("\n--- Contoh Tuple (immutable) ---")

	# Membuat tuple
	koordinat = (10.0, 20.0)
	print("Tuple koordinat:", koordinat)

	# Akses elemen mirip seperti list
	print("X:", koordinat[0], "Y:", koordinat[1])

	# Single-element tuple: perhatikan koma
	satu = (5,)
	bukan_tuple = (5)
	print("Single-element tuple (dengan koma):", satu, "tipe:", type(satu))
	print("Tanpa koma -> bukan tuple, tipe:", type(bukan_tuple))

	# Unpacking
	x, y = koordinat
	print("Unpacking -> x:", x, ", y:", y)

	# Tuple bersifat immutable — operasi seperti assign indeks akan error
	try:
		koordinat[0] = 0
	except TypeError as e:
		print("Error jika coba ubah tuple (immutable):", e)

	# Tetapi kita bisa membuat tuple baru dari elemen lama
	koordinat_baru = (0,) + koordinat[1:]
	print("Membuat tuple baru dari tuple lama:", koordinat_baru)

	# Konversi antara list <-> tuple
	lst = [1, 2, 3]
	tup = tuple(lst)
	print("Konversi list->tuple:", tup)
	lst2 = list(tup)
	print("Konversi tuple->list:", lst2)

	# Tuple bisa dipakai sebagai key di dict (jika berisi elemen yang hashable)
	posisi = {}
	posisi[(10, 20)] = "Lokasi A"
	print("Menggunakan tuple sebagai key dict:", posisi)


def pitfalls_examples():
	print("\n--- Contoh kesalahan umum / pitfalls ---")

	# Mengira tuple kosong dibuat dengan () vs koma
	empty_tuple = ()
	print("Tuple kosong:", empty_tuple)

	# Mengira (1) adalah tuple (bukan)
	print("(1) adalah", type((1)))

	# Single element list vs tuple
	print("[1] adalah", type([1]))

	# Perbedaan mutabilitas: contoh yang sering bikin bingung
	a_list = [1, 2, 3]
	a_ref = a_list
	a_ref.append(4)
	print("Mengubah a_ref mempengaruhi a_list (aliasing):", a_list)

	a_tuple = (1, 2, 3)
	a_ref_t = a_tuple
	# a_ref_t += (4,) membuat tuple baru, tidak mengubah tuple lama
	a_ref_t += (4,)
	print("a_tuple setelah operasi += di alias -> a_tuple masih:", a_tuple)
	print("a_ref_t menjadi:", a_ref_t)


def main():
	show_list_examples()
	show_tuple_examples()
	pitfalls_examples()


if __name__ == '__main__':
	main()

