#contoh penangkapan semua kesalahan

try:
    a = input("Masukkan angka pertama: ")
    b = input("Masukkan angka kedua: ")
    hslbg = int(a)/int(b)
    print("Hasil baginya: ", hslbg) 
except(ZeroDivisionError):
    print("Tidak boleh dibagi 0")
except (ValueError):
    print("Value Error, harus angka yang dimasukkan")
except (KeyboardInterrupt):
    print("Program dihentikan lewat keyboard")
else:
    print("Pangkat dua hasil baginya: ", hslbg**2)
finally:
    print("Akhirnya, selesai.")
