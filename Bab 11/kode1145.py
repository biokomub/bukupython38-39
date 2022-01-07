class Komponen:
    #konstruktor kelas komponen
    def __init__(self):
        print("Objek kelas Komponen dibuat!")
  
    #metode kelas komponen
    def metKomponen(self):
        print("Metode kelas Komponen dieksekusi!")
  
  
class Komposit:
    #konstruktor kelas komposit
    def __init__(self):
        #buat objek Komponen
        self.obj1 = Komponen()
        print("Objek kelas Komposit dibuat!")
  
    #metode kelas komponen
    def metKomposit(self):    
        print("Metode kelas Komposit dieksekusi!")
        #panggil metode komponen
        self.obj1.metKomponen()
  
  
#buat objek dari Komposit
obj2 = Komposit()
  
#panggil metode Komposit
obj2.metKomposit()
