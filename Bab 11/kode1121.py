class Kelas(object):
    "Ini hanya kelas kosong biasa"
    def __new__(cls): 
        return super(Kelas, cls).__new__(cls)  

    def __init__(self):
        pass
    
    def __del__(self):
        del self
        
    def metode():
        print("Ini hanya sebuah kelas")
        print("Bukan apa - apa")

#buat objek objKelas dari Kelas
objKelas = Kelas()

print("Atribut built-in Kelas")
print("Isi Kelas.__name__:", Kelas.__name__)
print("Isi Kelas.__doc__:", Kelas.__doc__)
print("Isi Kelas.__bases__:", Kelas.__bases__)
print("Isi Kelas.__module__:", Kelas.__module__)
print("Isi Kelas.__dir__:", Kelas.__dir__)
print("Isi Kelas.__dict__:", Kelas.__dict__)
print("======================")
print("Atribut built-in Kelas")
print("Isi objKelas.__doc__:", objKelas.__doc__)
print("Isi objKelas.__module__:", objKelas.__module__)
print("Isi objKelas.__dir__:", objKelas.__dir__)
print("Isi objKelas.__dict__:", objKelas.__dict__)
