nilai = ["nilai_lama"]

def PassByRef(nilai):
    #sebelum dilewatkan
    nilai = nilai
    print("Nilai di dalam fungsi",
          "sebelum argumen dilewatkan: ", nilai)
    print("Alamat Nilai di dalam fungsi",
          "sebelum argumen dilewatkan: ", id(nilai))
    #sesudah dilewatkan
    nilai_baru = "nilai_baru"
    nilai[0] = nilai_baru
    print("Nilai di dalam fungsi",
          "sesudah argumen dilewatkan: ", nilai)
    print("Alamat Nilai di dalam fungsi",
          "sesudah argumen dilewatkan: ", id(nilai))
    
    return 

print("Nilai di luar fungsi",
      "sebelum fungsi dipanggil: ", nilai)
print("Alamat Nilai di luar fungsi ",
      "sebelum fungsi dipanggil: ", id(nilai))

PassByRef(nilai)
print("Nilai di luar fungsi",
      "sesudah fungsi dipanggil: ", nilai)
print("Alamat Nilai di luar fungsi ",
      "sesudah fungsi dipanggil: ", id(nilai))
