import platform
import psutil as psu
import sys

try:
    sisop = platform.system()
    rilis = platform.release()
    arsitek = platform.machine()
    prosessor = platform.processor()
    mesin = platform.machine()
    ram = psu.virtual_memory()
    disk = ps.disk_usage('/')
except Exception as e:
    print(f"ada eror: {e}")
    sys.exc_info()

ramtotal = round(ram.total / (1024 ** 3),2) #menggunakan round
disktotal = disk.total / (1024 ** 3) #menggunakan float

print(f"Sistem Operasi : {sisop} {rilis}")
print(f"Arsitektur     : {arsitek}")
print(f"Prosessor      : {prosessor}")
print(f"Mesin          : {mesin}")
print("")
print(f"RAM            : {ram.total} bytes")
print(f"               : {ramtotal} GB")
print("")
print(f"Disk           : {disk.total} bytes")
print(f"               : {disktotal:.2f} GB")
