class kelasInduk(object):
    def __init__(self, a):
        self.a = a
    def cetakInduk(self):
        print("Ini nilai dari kelasInduk:", self.a)

class kelasAnak(kelasInduk):
    def __init__(self, induk, anak):
        #panggil __init__ kelasInduk
        kelasInduk.__init__(self, induk)
        #anak
        self.anak = anak
    def cetakAnak(self):
        print("Ini nilai khusus dari kelasAnak:", 
              self.anak)

#buat objek        
objAnak = kelasAnak(893, 1000)

objAnak.cetakInduk()
objAnak.cetakAnak()
