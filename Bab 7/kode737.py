#mendefinisikan kelas
class record_profil:
    nama = "Maulana"
    umur = 27 
    asal = "Malang"
    pekerjaan = "Penulis"
    asal_jurusan = "Biologi" 
    asal_pt = " Universitas Brawijaya" 
    angkatan = 2012

print("Halo, Semuanya! Perkenalkan, \
nama saya {r.nama}. \
Umur saya {r.umur} tahun. \
Saya berasal dari {r.asal}. \
Pekerjaan saya adalah {r.pekerjaan}. \
Dulu saya berkuliah di {r.asal_jurusan}{r.asal_pt} \
angkatan {r.angkatan}. \
Mohon kerjasamanya, terima kasih.".format(
  r=record_profil))
