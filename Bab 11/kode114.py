class SA(object):
    nama = "" #ini variabel kelas
    tipe = ""
    jabatan = "" 

    def __init__(self): #konstruktor
        pass

def inputData(object):
    a = input("Masukkan nama: ")
    b = input("Masukkan tipe: ")
    c = input("Masukkan jabatan: ")
    
    setattr(object, "nama", a)
    setattr(object, "tipe", b)
    setattr(object, "jabatan", c)
    
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
