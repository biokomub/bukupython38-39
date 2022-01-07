def bagi(a, b):
    x = a
    y = b
    hasil = x / y
    return hasil

#cetak
print(bagi(2, 4)) #tanpa kunci
print(bagi(a = 2, b = 4)) #diberi kunci
print(bagi(2, b = 4)) #campuran tanpa kunci – kunci 
print(bagi(a = 2, 4)) #campuran kunci – tanpa kunci 
print(bagi(b = 2, a = 4)) #posisi kunci dibalik
print(bagi(4, 2)) #posisi dibalik tanpa diberi kunci
