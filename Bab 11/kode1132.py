class Padi(object):
    def __init__(self, tinggi:int, umur_panen:int,
                 pg:float, lg:float, tg:float,
                 pb:float, lb:float, tb:float,
                 ka:float):
        self.tinggi = tinggi  
        self.umur_panen = umur_panen
        self.pg = pg 
        self.lg = lg
        self.tg = tg
        self.pb = pb
        self.lb = lb
        self.tb = tb
        self.ka = ka 

    def cetakData(self):
        print("Tinggi:", self.tinggi, "cm")
        print("Umur Panen:", self.umur_panen, "hari")
        print("Dimensi gabah:", self.pg, "x",
              self.lg, "x",
              self.tg, "mm")
        print("Dimensi beras:", self.pb, "x",
              self.lb, "x",
              self.tb, "mm")
        print("Kadar Amilosa:", self.ka)
    
    def klasifBeras(self):
        if ((float(self.pb)) >= 7.0):
            print("Ini beras tipe Bulir Panjang Kelas 1")
        elif (((float(self.pb)) >= 6.6) and \
              ((float(self.pb)) <= 7.0)):
            print("Ini beras tipe Bulir Panjang Kelas 2")
        elif (((float(self.pb)) >= 6.2) and \
              ((float(self.pb)) <= 6.6)):
            print("Ini beras tipe Bulir Panjang Kelas 3")
        elif ((float(self.pb)) <= 6.2):
            print("Ini beras tipe Bulir Pendek")
        else:
            print("Nilai panjang beras tidak valid")
            
    def klasifAmilosa(self):
        if ((float(self.ka)) < 13.0):
            print("Ini beras beramilosa rendah")
        elif (((float(self.ka)) >= 13.0) and \
              ((float(self.ka)) <= 20.0)):
            print("Ini beras beramilosa sedang")
        elif ((float(self.ka)) > 20.0):
            print("Ini beras beramilosa tinggi")
        else:
            print("Nilai amilosa beras tidak valid")
        
class PadiThailand(Padi):
    def __init__(self, nama_varietas, tinggi:int, 
                 umur_panen:int, pg:float, lg:float, 
                 tg:float, pb:float, lb:float, tb:float,
                 ka:float, prod:float,
                 info_ketahanan):
        #akses atribut dari kelas induk
        super(PadiThailand, self).__init__( 
             tinggi, umur_panen,
            pg, lg, tg,
            pb, lb, tb, ka)
        #atribut unik kelas anak
        self.nama_varietas = nama_varietas #perluasan
        self.prod = prod #perluasan
        self.info_ketahanan = info_ketahanan #perluasan
        
    def cetakData(self):
        print("Nama Varietas:", self.nama_varietas)
        #akses ke kelas induk
        super(PadiThailand, self).cetakData() 
        print("Produktivitas:", self.prod, "ton/ha")
        print("Ketahanan:", self.info_ketahanan)
        
#buat objek padi
objPadi = PadiThailand("RD41", "104", "105",
                       "10.40", "2.5", "2.0",
                       "7.7", "2.2", "1.8",
                       "27.16", "4.5", "Wereng Coklat")

objPadi.cetakData()
objPadi.klasifBeras()
objPadi.klasifAmilosa()
