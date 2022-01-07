class kelasX(object):
    def __new__(cls):
        print("Buat instance dari kelas kelasX")
        return super(kelasX, cls).__new__(cls)

    def __init__(self):
        print("Init kelas kelasX dipanggil")
                
class kelasA(object):
    def __new__(cls):
        print("Buat instance dari kelas kelasA")
        return kelasX()
  
    def __init__(self):
        print("Init kelas kelasA dipanggil")
        
kelasA()
