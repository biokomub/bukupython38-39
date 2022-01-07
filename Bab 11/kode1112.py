class kelasA(object):
    def __new__(cls):
        print("Buat instance dari kelas kelasA")
  
    def __init__(self):
        print("Init kelas kelasA dipanggil")
        
kelasA()
