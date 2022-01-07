from abc import ABCMeta, abstractmethod

#kelas abstrak
class Bangun3D(metaclass = ABCMeta):
    @abstractmethod 
    def IdBangun(self):
        pass
    @abstractmethod 
    def HitungLuasAlas(self):
        pass
    @abstractmethod 
    def HitungLuasPermukaan(self):
        pass
    @abstractmethod 
    def HitungVolume(self):
        pass

#kelas konkrit untuk bangun kotak
#bisa kubus, bisa kotak
class Kotak(Bangun3D):
    def __init__(self, p, l, t):        
        self.panjang = p
        self.lebar = l
        self.tinggi = t
        
        a = self.panjang
        b = self.lebar
        c = self.tinggi
        
        if ((((a == b) and (b == c)) and (a == c)) \
            == True):
            self.namaBangun = "Kubus"
        else:
            self.namaBangun = "Balok"
            
    def IdBangun(self):
        print("Nama Bangun 3D:", self.namaBangun)
        print("Panjang:", self.panjang)
        print("Lebar:", self.lebar)
        print("Tinggi:", self.tinggi)
    
    def HitungLuasAlas(self):
        a = self.panjang
        b = self.lebar
        l_alas = a * b
        print("Luas alas Bangun 3D:", l_alas)
        
    def HitungLuasPermukaan(self):
        a = self.panjang
        b = self.lebar
        c = self.tinggi
        
        if ((((a == b) and (b == c)) and (a == c)) \
            == True):
            l_permk = 6 * a * b
            print("Luas permukaan Bangun 3D:", l_permk)
        else:
            l_permk = (2 * a * b) + (2 * b * c) + \
                (2 * a * c)
            print("Luas permukaan Bangun 3D:", l_permk)
           
    def HitungVolume(self):
        a = self.panjang
        b = self.lebar
        c = self.tinggi
        vol = a * b * c
        print("Volume Bangun 3D:", vol)

obj1 = Kotak(6, 6, 6)
obj1.IdBangun()
obj1.HitungLuasAlas()
obj1.HitungLuasPermukaan()
obj1.HitungVolume()

obj2 = Kotak(7, 10, 12)
obj2.IdBangun()
obj2.HitungLuasAlas()
obj2.HitungLuasPermukaan()
obj2.HitungVolume()
