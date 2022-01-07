#mendapatkan atribut file

import pathlib
dirKerja = pathlib.Path("E:\TESTING\Test Folder")
for entri in dirKerja.iterdir():
    fileStat = entri.stat()
    print("============================")
    print("Tipe entri: ", ((type(entri)))) 
    print("Nama entri: ", entri.name) 
    print("Alamat entri: ", entri.absolute()) 
    print("Tipe Stat entri: ", ((type(fileStat))))
    print("Stat entri: ", fileStat)
