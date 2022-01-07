from multimethod import multimethod

class Contoh(object):
      
    @multimethod
    def ganda(self, x: int):
        return (2 * x)
  
    @multimethod
    def ganda(self, x: str):
        return (2 * x)
    
    @multimethod
    def ganda(self, x: complex):
        return ("Tidak menerima kompleks")
    
#pembuat objek dan caller  
obj = Contoh()
print("Hasil:", obj.ganda(3))
print("Hasil:", obj.ganda("Haha"))
print("Hasil:", obj.ganda(6j))
