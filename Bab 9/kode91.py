#membuat file

try:
    objFile = open("daftar pohon.txt", "x")
except BaseException as be:
    print("Error: ", be)
else:
    print("File berhasil dibuat!")
finally:
    objFile.close()
