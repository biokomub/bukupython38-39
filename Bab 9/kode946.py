#bekerja dengan fnmatch.fnmatch()

import os
import traceback as tb
import fnmatch

#tentukan direktori kerja
dirKerja = "E:\TESTING\Tugas Kuliah"

#temukan file berakhiran ".pdf" 
try:
    for namaFile in os.listdir(dirKerja):
        if fnmatch.fnmatch(namaFile, "*.pdf"):
            print(namaFile)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
