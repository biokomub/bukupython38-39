from multimethod import multimethod

class Contoh(object):
      
    @multimethod
    def tambah(self, x: int, y: int):
        return (x + y)
  
    @multimethod
    def tambah(self, x: str, y: str):
        return (x + y)
    
    @multimethod
    def tambah(self, x: complex, y: complex):
        return ("Tidak menerima kompleks")
    
#pembuat objek dan caller  
obj = Contoh()
print("Hasil:", obj.tambah(3, 7))
print("Hasil:", obj.tambah("Haha", "Hihi"))
print("Hasil:", obj.tambah(6j, 4j))
