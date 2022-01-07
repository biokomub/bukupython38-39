#membuka file

try:
    objFile = open("daftar pohon.txt", "w")
except BaseException as be:
    print("Error: ", be)
else:
    #tulis file
    objFile.write("Nama pohon   Nama latin\n")
    objFile.write("Aren         Arenga pinnata\n")
    objFile.write("Bintaro      Cerbera manghas\n")
    objFile.write("Durian       Durio zibethinus\n")
    objFile.write("Flamboyan    Delonix regia\n")
    objFile.write("Kantil       Magnolia x alba\n")
    objFile.write("Kelapa       Cocos nucifera\n")
    objFile.write("Kelapa Sawit Elaeis guineensis\n")
    objFile.write("Kelengkeng   Dimocarpus longan\n")
    objFile.write("Kenanga      Cananga odorata\n")
    objFile.write("Mahoni       Swietenia mahagoni\n")
    objFile.write("Manggis      Garcinia mangostana\n")
    objFile.write("Palem Raja   Roystonea regia\n")
    objFile.write("Rambutan     Nephelium lappaceum\n")
    objFile.write("Sukun        Artocarpus communis\n")
    objFile.write("Trembesi     Samanea saman\n")
    #cetak pesan berhasil
    print("File berhasil ditulis!")
finally:
    objFile.close()
