#ilustrasi pemodifikasi akses protected
 
#superkelas
class superclsKatak(object):
    
     #anggota data protected
     _namaKatak = None
     _namaLatin = None
     _origin = []
     _kodeVoucher = None
     _kodeAksNCBI = None
    
     #konstruktor superkelas
     def __init__(self, nama, nama_latin, 
                  origin, kode_voucher, kode_AksNCBI): 
          self._namaKatak = nama
          self._namaLatin = nama_latin
          self._origin = origin
          self._kodeVoucher = kode_voucher
          self._kodeAksNCBI = kode_AksNCBI
    
     #anggota fungsi/metode protected 
     def _tampilAsaldanNegara(self):
          #akses anggota data protected
          print("Tempat: ", self._origin[0])
          print("Negara: ", self._origin[1])

#subkelas
class SpesiesKatak(superclsKatak): 
     #konstruktor subkelas
     def __init__(self, nama, nama_latin, 
                  origin, kode_voucher, kode_AksNCBI):
         superclsKatak.__init__(self, nama, nama_latin, 
                                origin, kode_voucher, 
                                kode_AksNCBI)
         
     #anggota fungsi public     
     def tampilData(self):
           #mengakses data protected dari superkelas
           print("============================")
           print("Nama Katak: ", self._namaKatak)
           print("Nama Latin: ", self._namaLatin)
           print("Kode Voucher: ", self._kodeVoucher)
           print("Kode Aksesi NCBI: ", self._kodeAksNCBI)
           #mengakses fungsi/metode protected dari 
           #superkelas
           self._tampilAsaldanNegara()
    
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
