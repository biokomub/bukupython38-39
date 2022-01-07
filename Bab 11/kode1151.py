from multipledispatch import dispatch

class Contoh(object):
      
    @dispatch(int)
    def ganda(x):
        return (2 * x)
  
    @dispatch(str)
    def ganda(x):
        return (2 * x)
    
    @dispatch(complex)
    def ganda(x):
        return ("Tidak menerima kompleks")
    
#pembuat objek dan caller  
obj = Contoh()
print("Hasil:", obj.ganda(3))
print("Hasil:", obj.ganda("Haha"))
print("Hasil:", obj.ganda(6j))
