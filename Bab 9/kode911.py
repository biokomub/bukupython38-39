#mengoperasikan 2 file
#satu baca, satu tulis

fileOri = 'pohon taman.txt'
fileTujuan = 'pohon taman 2.txt'
with open(fileOri, 'r') as O, open(fileTujuan, 'w') as T:
    print("File original dibaca...")
    dataOri = O.readlines()
    print("File tujuan ditulis bacaan file original...")
    Tujuan.writelines(dataOri)
    print("Selesai!")
