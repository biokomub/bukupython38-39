#mendapatkan data waktu file/folder

import os
from datetime import datetime as dt
with os.scandir("E:\TESTING\Test Folder") as dirKerja:
    for entri in dirKerja:
        fileStat = entri.stat()
        
        wktAkses = dt.utcfromtimestamp(fileStat.st_atime)
        wktMod = dt.utcfromtimestamp(fileStat.st_mtime)
        wktUbahMD = dt.utcfromtimestamp(fileStat.st_ctime)

        print("============================")
        print("Tipe entri: ", ((type(entri)))) 
        print("Nama entri: ", entri.name) 
        print("Alamat entri: ", entri.path) 
        print("Tipe Stat entri: ", ((type(fileStat))))
        print("Stat entri: ", fileStat)
        print("Waktu Akses Terakhir: ", wktAkses)
        print("Waktu Modifikasi Terakhir: ", wktMod)
        print("Waktu Ubah Metadata Terakhir: ", wktUbahMD)
