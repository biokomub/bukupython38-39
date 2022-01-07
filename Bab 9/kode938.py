#mendapatkan daftar direktori dengan os.scandir()

import os
import traceback as tb

folder = r"E:\TESTING"

try:
    listDir = os.scandir(folder)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print("Listdir: ", listDir)
    print("Entri: ")
    for entri in listDir:
        print("-> ", entri)
