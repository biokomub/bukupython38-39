#bekerja dengan variabel substitusi di %-formatting 

#nama asli variabel
a = "Andri"
b = 28

#cetak dengan variabel substitusi
print("Nama saya %(nama)s, umur saya %(umur)i tahun." % \
    {"nama" : a, "umur" : b} \
     )
