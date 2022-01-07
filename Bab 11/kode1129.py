#buat kelas
class Tabung(object):
    def __init__(self, jari2, tinggi):
        self.pi = 22/7
        
        self.__rTabung = jari2
        self.__tTabung = tinggi
        
    #definisi properti volume tabung
    @property
    def volumeTabung(self):
        volTabung = self.pi * \
                    (self.__rTabung) ** 2 * \
                    self.__tTabung
        return round(volTabung, 2)
        
    #definisi properti luas permukaan tabung
    @property
    def lptTabung(self):
        lptTabung = 2 * self.pi * \
                        self.__rTabung * \
                        (self.__rTabung + self.__tTabung)
        return round(lptTabung, 2)

#parameter tabung        
rTabung = 5
tTabung = 15

#buat objek tabung
objTabung = Tabung(rTabung, tTabung)        

#panggil metode
print("Jari - Jari Tabung:", rTabung)
print("Tinggi Tabung:", tTabung)
print("Volume Tabung:", objTabung.volumeTabung)
print("Luas Permukaan Tabung:", objTabung.lptTabung)
