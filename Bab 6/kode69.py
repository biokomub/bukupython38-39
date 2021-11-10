#contoh try... except... finally...

try:
    a = input("Masukkan angka pertama: ")
    b = input("Masukkan angka kedua: ")
    hslbg = int(a)/int(b)
    print("Hasil baginya: ", hslbg) 
except (ValueError, ZeroDivisionError):
    print("Ada yang salah...")
finally:
    print("Akhirnya, selesai.")
