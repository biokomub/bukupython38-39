#membaca file dan menampilkannya ke layar

try:
    objFile = open("daftar pohon.txt", "r")
    line = objFile.readline() #inisiasi file.readline()
    while line != '':  # Tanda EOF adalah string kosong
        print(line, end='')
        line = objFile.readline()
except BaseException as be:
    print('Error: ', be)
finally:
    objFile.close()
