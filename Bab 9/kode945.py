#bekerja dengan startswith()

import os
import traceback as tb

#tentukan direktori kerja
dirKerja = "E:\TESTING\Tugas Kuliah"

#temukan file berawalan "jurnal" 
try:
    for namaFile in os.listdir(dirKerja):
        if namaFile.startswith("jurnal"):
            print(namaFile)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
