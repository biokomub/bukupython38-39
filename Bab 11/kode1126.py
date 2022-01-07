#buat kelas
class Koordinat(object):
    def __init__(self, nama = None, x = None, y = None):
        self.__nama = nama
        self.__x = x
        self.__y = y

    def getNama(self):
        return self.__nama

    def setNama(self, nama):
        self.__nama = nama
    
    def delNama(self):
        print("Deleter nama dipanggil")
        del self.__nama
    
    def getx(self):
        return self.__x

    def setx(self, x):
        self.__x = x 

    def gety(self):
        return self.__y

    def sety(self, y):
        self.__y = y 


#buat objek        
titik = Koordinat()

#set objek
titik.setNama("A")
titik.setx(1)
titik.sety(2)

#ambil data
print("Titik %s terletak di (%d, %d)" 
      % (titik.getNama(), titik.getx(), titik.gety()))

#ubah nama titik
titik.setNama("B")

#ambil data
print("Nama diganti")
print("Titik %s terletak di (%d, %d)" 
      % (titik.getNama(), titik.getx(), titik.gety()))

#hapus nama titik
titik.delNama()
