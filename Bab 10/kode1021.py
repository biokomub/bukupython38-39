def tugaskanAngka(angka):
    print("Panggil fungsi tugaskanAngka()")
    print("Nilai Angka dalam fungsi sebelum penugasan:", 
          angka, ", alamat:", id(angka))
    print("Beri penugasan ...")
    print("Angka akan ditambah 69")
    angka = angka + 69
    print("Nilai Angka dalam fungsi sesudah penugasan:", 
          angka, ", alamat:", id(angka))
        
angka = 10

print("===Sebelum fungsi dipanggil===")
print("Nilai Angka di luar fungsi sebelum pemanggilan:", 
      angka, ", alamat:", id(angka))

print("===Panggil fungsi===")
tugaskanAngka(angka)

print("===Setelah fungsi dipanggil===")
print("Nilai Angka di luar fungsi sesudah pemanggilan:", 
      angka, ", alamat:", id(angka))
