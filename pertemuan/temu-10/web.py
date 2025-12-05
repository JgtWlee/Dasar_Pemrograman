import platform
import psutil
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    sistem = platform.system()
    rilis = platform.release()
    arsitektur = platform.architecture()
    processor = platform.processor()
    mesin = platform.machine()

    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    total_ram_gb = round(ram.total / (1024**3), 2)
    total_disk_gb = round(disk.total / (1024**3), 2)

    return f"""
    Sistem Operasi : {sistem} {rilis} <br>
    Arsitektur     : {arsitektur} <br>
    Prosesor       : {processor} <br>
    Mesin          : {mesin} <br>
    <br>
    RAM            : {ram.total} <br>
    RAM dalam GB   : {total_ram_gb} GB <br>
    <br>
    Disk           : {disk.total} <br>
    Disk dalam GB  : {total_disk_gb:.2f} GB
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
