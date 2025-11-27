import sys

lists = ['a', 0, 4]
for each in lists:
    try:
        print("Masukan:", each)
        hasil = 1/int(each)
        break
    except ValueError:
        print(f"Error wak {each} bukan angka")

    except ZeroDivisionError:
        print("Error wak, ga bisa dibagi nol")

    except Exception as e:
        print(f"Error tak terduga: {e}")

print("Program selesai")
   