#membuat pohon direktori

import os
import pathlib

#ini konstanta berisi komponen
#pembentuk grafis pohon
PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

#ini kelas yang bisa dipanggil
class PohonDirektori:
    #inisiasi kelas
    def __init__(self, root_dir):
        #buat instance atribut _generator 
        #objek PohonDirektori
        #instance ini berisi 
        #_PembangunPohon dari root_dir
        #root_dir = direktori yang menjadi akar
        #bisa direktori kerja atau yang dikerjakan
        self._generator = _PembangunPohon(root_dir)
    
    #buat pohon direktori
    def buat_pohon_dir(self):
        #bangun pohon melalui _generator
        #karena _generator berisi _PembangunPohon,
        #maka _generator bisa mempunyai atribut
        #layaknya _PembangunPohon
        pohon = self._generator.bangun_pohon()
        #cetak entri dalam pohon
        for entri in pohon:
            print(entri)

#ini kelas internal "_class"
#tidak bisa dipanggil langsung
#kecuali oleh kelas yang lain 
class _PembangunPohon:
    #inisiasi kelas
    def __init__(self, root_dir):
        #tetapkan atribut
        #_root_dir merupakan path 
        self._root_dir = pathlib.Path(root_dir)
        #tetapkan atribut
        #_pohon berupa objek kosong
        self._pohon = []

    #bangun pohon
    def bangun_pohon(self):
        #buat kepala pohon
        self._kepala_pohon()
        #buat badan pohon
        self._badan_pohon(self._root_dir)
        #kembalikan hasil metode
        #menjadi atribut _pohon
        return self._pohon
    
    #buat kepala pohon
    def _kepala_pohon(self):
        #append string path _root_dir
        #dengan separator os.sep
        #untuk kepala pohon
        self._pohon.append(f"{self._root_dir}{os.sep}")
        #append PIPE di bawah kepala pohon
        self._pohon.append(PIPE)
        
    #buat badan pohon
    def _badan_pohon(self, direktori, prefix=""):
        #isi entri - entri direktori
        #dengan pathlib.Path.iterdir()
        entri2 = direktori.iterdir()
        #sort agar folder didahulukan
        #baru file
        entri2 = sorted(entri2, 
                        key=lambda entri: entri.is_file())
        #hitung jumlah entri – entri pada direktori
        jumlah_entri2 = len(entri2)
        #perulangan untuk setiap indeks and entri
        #dalam enumerasi entri - entri data
        #enumerasi dengan enumerate()
        #bertujuan untuk mengasosiasi indeks dengan entri
        for indeks, entri in enumerate(entri2):
            #hubungkan dengan ELBOW
            #jika indeks == (jumlah entri - entri) - 1 
            #jika tidak, hubungkan dengan TEE
            if (indeks == jumlah_entri2 - 1): 
                penghubung = ELBOW
            else: 
                penghubung = TEE
            #tambahkan eksepsi try... except.. di sini!
            #eksepsi akan mencegah OSError saat iterasi 
            #objek iterdir dikarenakan kurang akses
            #kepada folder tertentu pada src original,
            #ini tidak dieksepsi, sehingga 
            #selalu error
            #Lihat: 
            #https://stackoverflow.com/questions/28014915/
            #python-pathlib-avoid-permission-errors-when-
            #using-iterdir
            try:
                #jika entri adalah direktori
                if entri.is_dir():
                    #maka tambah struktur direktori ke 
                    #pohon
                    self._tambah_direktori(
                        entri, indeks, jumlah_entri2, 
                        prefix, penghubung
                        )
                #jika entri adalah bukan direktori,
                #tapi file
                else: 
                    #maka tambah struktur direktori ke 
                    #pohon
                    self._tambah_file(
                        entri, prefix, penghubung)
            except OSError:
                pass

    #tambah direktori
    def _tambah_direktori(
        self, direktori, indeks, 
        jumlah_entri2, prefix, penghubung
    ):
        #append pohon dengan: 
        #prefix, penghubung, nama direktori, dan separator 
        self._pohon.append(
            f"{prefix}{penghubung} {direktori.name}{os.sep}")
        #jika indeks tidak sama dengan
        # (jumlah entri - entri) - 1
        if indeks != jumlah_entri2 - 1:
            #gunakan PIPE_PREFIX kepada
            #prefix penghubung yang sudah ada
            prefix += PIPE_PREFIX
        else:
            #gunakan PIPE_PREFIX kepada
            #prefix penghubung yang sudah ada
            prefix += SPACE_PREFIX
        #buat _badan_pohon 
        #berisi direktori dan prefix
        self._badan_pohon(
            direktori=direktori,
            prefix=prefix,
        )
        #append rstrip karakter kosong pada prefix
        #ke _pohon
        self._pohon.append(prefix.rstrip())
    
    #tambah file
    def _tambah_file(self, file, prefix, penghubung):
        #append prefiks, penghubung, nama file
        #ke _pohon
        self._pohon.append(
            f"{prefix}{penghubung} {file.name}")

################################################################

#lakukan listing direktori

import traceback as tb

tujuan = r"E:\TESTING" #direktori yang kita listing

try:
    pohon = PohonDirektori(tujuan)
    pohon.buat_pohon_dir() #
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
