class kelasInduk1(object):
    def __init__(self, a):
        self.a = a
    def cetak1(self):
        print("Ini nilai dari kelasInduk1:", self.a)

class kelasInduk2(object):
    def __init__(self, b):
        self.b = b
    def cetak2(self):
        print("Ini nilai dari kelasInduk2:", self.b)

class kelasInduk3(object):
    def __init__(self, c):
        self.c = c
    def cetak3(self):
        print("Ini nilai dari kelasInduk3:", self.c)

class kelasAnak(kelasInduk1, kelasInduk2, kelasInduk3):
    def __init__(self, induk1, induk2, induk3, anak):
        #panggil __init__ kelasInduk1
        kelasInduk1.__init__(self, induk1)
        #panggil __init__ kelasInduk2
        kelasInduk2.__init__(self, induk2)
        #panggil __init__ kelasInduk3
        kelasInduk3.__init__(self, induk3)
        #anak
        self.anak = anak
    def cetakAnak(self):
        print("Ini nilai khusus dari kelasAnak:", 
              self.anak)

#buat objek        
objAnak = kelasAnak(124, 234, 346, 1000)

objAnak.cetak1()
objAnak.cetak2()
objAnak.cetak3()
objAnak.cetakAnak()
