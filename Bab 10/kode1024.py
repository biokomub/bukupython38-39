def tugaskanList(List):
    print("Panggil fungsi tugaskanList()")
    print("Nilai List dalam fungsi sebelum penugasan:", 
          List, ", alamat:", id(List))
    print("Beri penugasan ...")
    print("List ditambahkan")
    List += ["Mangga", "Jambu"]
    print("Nilai List dalam fungsi sesudah penugasan:", 
          List, ", alamat:", id(List))
        
List = ["Apel", "Belimbing", "Cempedak"]

print("===Sebelum fungsi dipanggil===")
print("Nilai List di luar fungsi sebelum pemanggilan:", 
      List, ", alamat:", id(List))

print("===Panggil fungsi===")
tugaskanList(List)

print("===Setelah fungsi dipanggil===")
print("Nilai List di luar fungsi sesudah pemanggilan:", 
      List, ", alamat:", id(List))
