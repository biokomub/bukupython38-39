def tugaskanString(string):
    print("Panggil fungsi tugaskanString()")
    print("Nilai String dalam fungsi sebelum penugasan:", 
          string, ", alamat:", id(string))
    print("Beri penugasan ...")
    print("String di konkatenasi")
    string = string + " dan IPA"
    print("Nilai Angka dalam fungsi sesudah penugasan:", 
          string, ", alamat:", id(string))
        
string = "Matematika"

print("===Sebelum fungsi dipanggil===")
print("Nilai String di luar fungsi sebelum pemanggilan:", 
      string, ", alamat:", id(string))

print("===Panggil fungsi===")
tugaskanString(string)

print("===Setelah fungsi dipanggil===")
print("Nilai String di luar fungsi sesudah pemanggilan:", 
      string, ", alamat:", id(string))
