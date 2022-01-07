from multipledispatch import dispatch

class Contoh(object):
      
    @dispatch(int, int)
    def tambah(x, y):
        return (x + y)
  
    @dispatch(str, str)
    def tambah(x, y):
        return (x + y)
    
    @dispatch(complex, complex)
    def tambah(x, y):
        return ("Tidak menerima kompleks")
    
#pembuat objek dan caller  
obj = Contoh()
print("Hasil:", obj.tambah(3, 7))
print("Hasil:", obj.tambah("Haha", "Hihi"))
print("Hasil:", obj.tambah(6j, 4j))
