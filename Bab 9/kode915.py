#mendapatkan atribut tipe file/folder dan izin akses

import os
with os.scandir("E:\TESTING\Test Folder") as dirKerja:
    for entri in dirKerja:
        fileStat = entri.stat()
        fileModeBits = fileStat.st_mode
        o_fileModeBits = oct(fileModeBits)
        
        if o_fileModeBits[:-3] == "0o100":
            fileType = "File"
        elif o_fileModeBits[:-3] == "0o40":
            fileType = "Folder"
        else:
            fileType = "Bukan File ataupun Folder"
        
        print("============================")
        print("Tipe entri: ", ((type(entri)))) 
        print("Nama entri: ", entri.name) 
        print("Alamat entri: ", entri.path) 
        print("Tipe Stat entri: ", ((type(fileStat))))
        print("Stat entri: ", fileStat)
        print("File Mode Bits: ", o_fileModeBits)
        print("Tipe File: ", o_fileModeBits[:-3], "->", 
              fileType)
        print("Izin Akses: ", o_fileModeBits[-3:])
