class Kelas(object): #ini kelas kosong
    def __new__(cls): 
        return super(Kelas, cls).__new__(cls)  

    def __init__(self):
        pass
    
    def __del__(self):
        del self

#cetak dir() dan vars()
print("Daftar dir() kelas Kelas():", dir(Kelas))
print("Daftar vars() kelas Kelas():", vars(Kelas))
