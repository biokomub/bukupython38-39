class SA(object):
    nama = "" #ini variabel kelas
    tipe = ""
    jabatan = "" 

    def __init__(self): #konstruktor
        pass

    def inputData(self):
        self.nama = input("Masukkan nama: ")
        self.tipe = input("Masukkan tipe: ")
        self.jabatan = input("Masukkan jabatan: ")
    
    def tampilData(self): 
        print("Nama    : ", self.nama)
        print("Tipe    : ", self.tipe)
        print("Jabatan : ", self.jabatan)
        print("")

#buat objek
SivitasAkademik = SA()
#entri data
print("Masukkan Data disini")
SivitasAkademik.inputData()
#cetak data
print("--------------------")
print("Cetak Data")
SivitasAkademik.tampilData()
