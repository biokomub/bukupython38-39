class kelasA(object):
    def __new__(cls):
        print("Buat instance dari kelas kelasA")
        return super(kelasA, cls).__new__(cls)
  
    def __init__(self):
        print("Init kelas kelasA dipanggil")
        
kelasA()
