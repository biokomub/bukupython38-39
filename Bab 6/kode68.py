#contoh try... except... else... 

try:
    a = input("Masukkan angka pertama: ")
    b = input("Masukkan angka kedua: ")
    hslbg = int(a)/int(b)
    print("Hasil baginya: ", hslbg) 
except (ValueError, ZeroDivisionError):
    print("Ada yang salah...")
else:
    print("Pangkat dua hasil baginya: ", hslbg**2)
