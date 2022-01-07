#mendapatkan atribut file

import os
with os.scandir("E:\TESTING\Test Folder") as dirKerja:
    for entri in dirKerja:
        fileStat = entri.stat()
        print("============================")
        print("Tipe entri: ", ((type(entri)))) 
        print("Nama entri: ", entri.name) 
        print("Alamat entri: ", entri.path) 
        print("Tipe Stat entri: ", ((type(fileStat))))
        print("Stat entri: ", fileStat)
