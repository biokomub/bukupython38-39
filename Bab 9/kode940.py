#mendapatkan daftar direktori dengan pathlib.Path.iterdir()

from pathlib import Path
import traceback as tb

folder = r"E:\TESTING"

try:
    dirPath = Path(folder)
    listDir = dirPath.iterdir()
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print("Listdir: ", listDir)
    print("Entri: ")
    for entri in listDir:
        print("-> ", entri)
