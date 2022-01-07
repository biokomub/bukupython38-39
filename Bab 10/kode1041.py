def hubungkanSistem(user, k_a, *MK, **IDs):
    print("Hubungkan sistem...")
    print("Nama anda:", user) 
    print("Kode akses:", k_a)
    print("Sistem terhubung! Selamat datang", user)
    print("Informasi IDs:", IDs)
    print("Mata Kuliah yang diasistensi:", MK)

hubungkanSistem("asisten", "6", 
                "MAB4137", "MAB4102",
                nama = "Maulana", nim = "125090100111004"
                )
