#membaca dan menampilkannya ke layar

try:
    objFile = open("daftar pohon.txt", "r")
    for i in (objFile):
        print(i)
except BaseException as be:
    print('Error: ', be)
finally:
    objFile.close()
