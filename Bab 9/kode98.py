#membaca dan menampilkannya ke layar

try:
    objFile = open("daftar pohon.txt", "r")
    line = objFile.readline() #inisiasi file.readline()
    # Baca dan cetak seluruh file baris per baris
    for line in (objFile):
        print(line, end='')
except BaseException as be:
    print('Error: ', be)
finally:
    objFile.close()
