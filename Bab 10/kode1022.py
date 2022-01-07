def tugaskanAngka(angka):
    print("Panggil fungsi tugaskanAngka()")
    print("Nilai Angka dalam fungsi sebelum penugasan:", 
          angka, ", alamat:", id(angka))
    print("Beri penugasan ...")
    print("Angka akan ditambah 69")
    angka += 69
    print("Nilai Angka dalam fungsi sesudah penugasan:", 
          angka, ", alamat:", id(angka))
        
num = 10

print("===Sebelum fungsi dipanggil===")
print("Nilai Angka di luar fungsi sebelum pemanggilan:", 
      num, ", alamat:", id(num))

print("===Panggil fungsi===")
tugaskanAngka(num)

print("===Setelah fungsi dipanggil===")
print("Nilai Angka di luar fungsi sesudah pemanggilan:", 
      num, ", alamat:", id(num))
