#menelusuri folder secara down-top

import os
import traceback as tb

#tentukan direktori kerja
dirKerja = "E:\TESTING"

#telusuri folder" 
try:
    print("Posisi folder kerja: ", dirKerja)
    #dpath = path direktori 
    #dnames = nama2 direktori
    #f = kumpulan file
    #fnames = nama2 file
    for dpath, dnames, f in os.walk(dirKerja,
                                    topdown = False):
        if dnames == []:
            print("")
            print("Tidak ada subfolder di", 
                  dpath, ", tapi ada file bernama:")
            for fnames in f:
                print(fnames)
        else:
            print("")
            print("Menemukan subfolder", dnames, 
                  "di", dpath, ", dan ada file di",
                  dpath, "bernama: ")
            for fname in f:
                print(fnames)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
