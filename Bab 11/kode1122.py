#ilustrasi penggunaan modifikasi akses publik
 
class Katak(object): 
     #konstruktor
     def __init__(self, nama, nama_latin):
           # angota data public
           self.namaKatak = nama
           self.namaLatin = nama_latin
 
     #anggota fungsi/metode public     
     def tampilData(self):
           # mengakses data public
           print("Akses data dari dalam kelas")
           print("Nama Katak: ", self.namaKatak)
           print("Nama Latin: ", self.namaLatin)
    
#membuat objek
objKatak1 = Katak("Kodok Sawah", 
                  "Fejervarya cancrivora")
 
#mengakses data public
print("Akses data dari luar kelas")
print("Nama Katak: ", objKatak1.namaKatak)
print("Nama Latin: ", objKatak1.namaLatin)
 
#memanggil anggota fungsi publik dari 
#objek turunan kelas
objKatak1.tampilData()
