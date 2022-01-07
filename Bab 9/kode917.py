#beda shutil.copy() dan shutil.copy2()dalam mengkopi file
#dilihat dari metadatanya

import os
import shutil
from datetime import datetime as dt
import traceback as tb

try:
    shutil.copy(r"E:\TESTING\Test Folder\readme.txt", 
                r"E:\TESTING\Test Folder\readmeCopy.txt")
    shutil.copy2(r"E:\TESTING\Test Folder\readme.txt", 
                r"E:\TESTING\Test Folder\readmeCopy2.txt")
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    #cek metadata file hasil kopi
    with os.scandir("E:\TESTING\Test Folder") as dirKerja:
        for entri in dirKerja:
            #dapatkan stat dari file
            fileStat = entri.stat()
            #dapatkan modebit file 
            fileModeBits = fileStat.st_mode
            o_fileModeBits = oct(fileModeBits)
        
            if o_fileModeBits[:-3] == "0o100":
                fileType = "File" #kita butuh tipe file File
                #dapatkan data waktu file
                wktAkses = \
                    dt.utcfromtimestamp(fileStat.st_atime)
                wktMod = \
                    dt.utcfromtimestamp(fileStat.st_mtime)
                wktUbahMD = \
                    dt.utcfromtimestamp(fileStat.st_ctime)
                #cetak informasi file
                print("============================")
                print("Tipe entri: ", 
                      ((type(entri)))) 
                print("Nama entri: ", 
                      entri.name) 
                print("Alamat entri: ", 
                      entri.path) 
                print("Tipe Stat entri: ", 
                      ((type(fileStat))))
                print("Stat entri: ", 
                      fileStat)
                print("Waktu Akses Terakhir: ", 
                      wktAkses)
                print("Waktu Modifikasi Terakhir: ", 
                      wktMod)
                print("Waktu Ubah Metadata Terakhir: ", 
                      wktUbahMD)
                print("Izin Akses: ",
                      o_fileModeBits[-3:])
            elif o_fileModeBits[:-3] == "0o40":
                fileType = "Folder"
                break #keluar dari perulangan, 
                      #kita tak butuh ini saat ini
            else:
                fileType = "Bukan File ataupun Folder"
                break #keluar dari perulangan, 
                      #kita tak butuh ini saat ini
