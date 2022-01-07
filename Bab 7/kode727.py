#nama asli variabel
a = "Benny"
b = 42

#cetak dengan mode default
print("Nama saya {}, umur saya {} tahun.".format(
    a, b)
    )

#cetak dengan positional-based param/args
#(indeks ditulis eksplisit)
print("Nama saya {0}, umur saya {1} tahun.".format(
    a, b)
    )

#cetak dengan keyword-based params/args
#(menggunakan kunci) 
print("Nama saya {nama}, umur saya {umur} tahun.".format(
    nama = a, umur = b)
    )

#cetak dengan mode argumen campuran
#(mixed arguments)
print("Nama saya {0}, umur saya {umur} tahun.".format(
    a, umur = b)
    )
