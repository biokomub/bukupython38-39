class SA(object):
    nama = "" #ini variabel kelas
    tipe = ""
    jabatan = "" 

    def __init__(self, nama, tipe, jabatan): #konstruktor
        self.nama = nama
        self.tipe = tipe
        self.jabatan = jabatan

    def tampilData(self): #metode untuk menampilkan data
        print("Nama    : ", self.nama)
        print("Tipe    : ", self.tipe)
        print("Jabatan : ", self.jabatan)
        print("")

#membuat objek sivitas akademika
org1 = SA("Prof. Widodo, Ph.D.Med.Sc.",
          "Dosen",
          "Dekan FMIPA UB")

org2 = SA("Prof. Muhaimin Rifa'i, Ph.D.Med.Sc",
          "Dosen",
          "Ketua Jurusan Biologi UB")

org3 = SA("Dr. Brian Rahardi",
          "Dosen",
          "Dosen Biologi UB")

org4 = SA("Ismail Marjuki",
          "Tenaga Kependidikan",
          "Staf TU Biologi UB")

#tampilkan data
org1.tampilData()
org2.tampilData()
org3.tampilData()
org4.tampilData()
