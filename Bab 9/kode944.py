#bekerja dengan endswith()

import os
import traceback as tb

#tentukan direktori kerja
dirKerja = "E:\TESTING\Tugas Kuliah"

#temukan file berakhiran ".pdf" 
try:
    for namaFile in os.listdir(dirKerja):
        if namaFile.endswith(".pdf"):
            print(namaFile)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
