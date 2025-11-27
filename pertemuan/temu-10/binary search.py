


def BinSearch(data, key):
    """Lakukan binary search pada daftar terurut 'data' untuk mencari 'key'.
    Mengembalikan indeks (0-based) jika ditemukan, atau -1 jika tidak ditemukan.
    Juga mencetak hasil pencarian.
    """
    awal = 0
    akhir = len(data) - 1
    ketemu = False
    posisi = -1

    while awal <= akhir and not ketemu:
        tengah = (awal + akhir) // 2
        if key == data[tengah]:
            ketemu = True
            posisi = tengah
            print('data', key, 'ditemukan di posisi', tengah)
        elif key < data[tengah]:
            akhir = tengah - 1
        else:
            awal = tengah + 1

    if not ketemu:
        print('data tidak ditemukan')

    return posisi


if __name__ == '__main__':
    data = [1, 3, 9, 11, 15, 22, 29, 31, 48]
    # contoh: cari 3 (harus ditemukan di indeks 1)
    idx = BinSearch(data, 3)
    print('return value:', idx)