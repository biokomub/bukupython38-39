#buat kelas
class Koordinat(object):
    def __init__(self, nama = None, x = None, y = None):
        self.__nama = nama
        self.__x = x
        self.__y = y

    def getnama(self):
        print("Ambil nama")
        return self.__nama

    def setnama(self, nilai):
        print("Set nama ke " + nilai)
        self.__nama = nilai

    def hapusnama(self):
        print("Hapus nama")
        del self.__nama
    
    #set properti nama di sini
    nama = property(getnama, setnama, hapusnama,
                    "Ini Properti nama")
        
    def getx(self):
        print("Ambil x")
        return self.__x

    def setx(self, nilai):
        print("Set x ke " + nilai)
        self.__x = nilai

    def hapusx(self):
        print("Hapus x")
        del self.__x
        
    #set properti x di sini
    x = property(getx, setx, hapusx,
                 "Ini Properti x")
        
    def gety(self):
        print("Ambil y")
        return self.__y

    def sety(self, nilai):
        print("Set y ke " + nilai)
        self.__y = nilai

    def hapusy(self):
        print("Hapus y")
        del self.__y
        
    #set properti y di sini
    y = property(getx, setx, hapusx,
                 "Ini Properti x")

#buat titik
titik = Koordinat("A", 1, 2)

#ambil data
print("Titik %s terletak di (%d, %d)" 
      % (titik.nama, titik.x, titik.y))

#ubah nama titik
titik.nama = "B"

#ambil data
print("Nama diganti")
print("Titik %s terletak di (%d, %d)" 
      % (titik.nama, titik.x, titik.y))

#hapus nama titik
del titik.nama
