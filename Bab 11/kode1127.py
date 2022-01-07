#buat kelas
class Koordinat(object):
    def __init__(self, nama = None, x = None, y = None):
        self.__nama = nama
        self.__x = x
        self.__y = y

    @property #juga berperan sebagai getter
    def nama(self):
        print("Ambil nama")
        return self.__nama

    @nama.setter
    def nama(self, nilai):
        print("Set nama ke " + nilai)
        self.__nama = nilai

    @nama.deleter
    def nama(self):
        print("Hapus nama")
        del self.__nama
            
    @property
    def x(self):
        print("Ambil x")
        return self.__x

    @x.setter
    def x(self, nilai):
        print("Set x ke " + nilai)
        self.__x = nilai

    @x.deleter
    def x(self):
        print("Hapus x")
        del self.__x
        
    @property
    def y(self):
        print("Ambil y")
        return self.__y

    @y.setter
    def y(self, nilai):
        print("Set y ke " + nilai)
        self.__y = nilai

    @y.deleter
    def y(self):
        print("Hapus y")
        del self.__y

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
