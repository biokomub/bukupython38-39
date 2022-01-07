#ilustrasi pemodifikasi akses private
 
class SpesiesKatak(object):
    
     #anggota data private
     __namaKatak = None
     __namaLatin = None
     __origin = []
     __kodeVoucher = None
     __kodeAksNCBI = None
    
     #konstruktor superkelas
     def __init__(self, nama, nama_latin, 
                  origin, kode_voucher, kode_AksNCBI): 
          self.__namaKatak = nama
          self.__namaLatin = nama_latin
          self.__origin = origin
          self.__kodeVoucher = kode_voucher
          self.__kodeAksNCBI = kode_AksNCBI
    
     #anggota fungsi/metode private 
     def __tampilAsaldanNegara(self):
          #akses anggota data private
          print("Tempat: ", self.__origin[0])
          print("Negara: ", self.__origin[1])
      
     #anggota fungsi public     
     def tampilData(self):
           #mengakses data protected dari superkelas
           print("============================")
           print("Nama Katak: ", self.__namaKatak)
           print("Nama Latin: ", self.__namaLatin)
           print("Kode Voucher: ", self.__kodeVoucher)
           print("Kode Aksesi NCBI: ", self.__kodeAksNCBI)
           #mengakses fungsi/metode protected dari 
           #superkelas
           self.__tampilAsaldanNegara()
  
#membuat objek
objKatak1 = SpesiesKatak("Kodok", 
                         "Fejervarya moodiei",
                         ["Ko Samui", "Thailand"],
                         "ZMKU AM 01387", "MN453500")
objKatak2 = SpesiesKatak("Kodok Iskandar", 
                         "Fejervarya iskandari",
                         ["Malang", "Indonesia"],
                         "-", "AB570268")
objKatak3 = SpesiesKatak("Kodok Sawah", 
                         "Fejervarya cancrivora",
                         ["Pak Phanang", "Thailand"],
                         "ZMKU AM 01511", "MN453527")
objKatak4 = SpesiesKatak("Bancet Hijau", 
                         "Occidozyga lima",
                         ["Kuala Lumpur", "Malaysia"],
                         "-", "AB488903")

#tampil data lewat fungsi publik dari 
#objek turunan kelas
objKatak1.tampilData()
objKatak2.tampilData()
objKatak3.tampilData()
objKatak4.tampilData() 
