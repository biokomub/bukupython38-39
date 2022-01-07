#membaca dan menampilkannya ke layar

try:
    objFile = open("daftar pohon.txt", "r")
    for i in (objFile):
        print(i, end='')
except BaseException as be:
    print('Error: ', be)
finally:
    objFile.close()
