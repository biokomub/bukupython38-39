class SA(object):
    nama = "" #ini variabel kelas
    tipe = ""
    jabatan = "" 

    def __init__(self, nama, tipe, jabatan): #konstruktor
        print("Konstruktor dipanggil\n")     
        self.nama = nama
        self.tipe = tipe
        self.jabatan = jabatan
 
    def __del__(self):
        print("Destruktor dipanggil")
        print("Data dibersihkan")
        del self.nama
        del self.tipe
        del self.jabatan

    def tampilData(self): #metode untuk menampilkan data
        print("Tampil Data")
        print("Nama    : ", self.nama)
        print("Tipe    : ", self.tipe)
        print("Jabatan : ", self.jabatan)
        print("")


org3 = SA("Dr. Brian Rahardi",
          "Dosen",
          "Dosen Biologi UB")

del org3
