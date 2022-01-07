#membaca file

try:
    objFile = open("daftar pohon.txt", "r")
    reader = objFile.read() #baca keseluruhan file
    print(reader) #paksa cetak, atau tidak muncul ke layar
except BaseException as be:
    print('Error: ', be)
finally:
    objFile.close()
