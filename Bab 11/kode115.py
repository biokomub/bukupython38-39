class SA(object):
    nama = "" #ini variabel kelas
    tipe = ""
    jabatan = "" 

    def __init__(self): #konstruktor
        pass

def inputData(object):
    object.nama = input("Masukkan nama: ")
    object.tipe = input("Masukkan tipe: ")
    object.jabatan = input("Masukkan jabatan: ")
    
def tampilData(object): 
    print("Nama    : ", (getattr(object, "nama")))
    print("Tipe    : ", (getattr(object, "tipe")))
    print("Jabatan : ", (getattr(object, "jabatan")))
    print("")

#buat objek
SivitasAkademik = SA()
#entri data
print("Masukkan Data disini")
inputData(SivitasAkademik)
#cetak data
print("--------------------")
print("Cetak Data")
tampilData(SivitasAkademik)
