def hubungkanSistem(user, k_a, **IDs, *MK):
    print("Hubungkan sistem...")
    print("Nama anda:", user) 
    print("Kode akses:", k_a)
    print("Sistem terhubung! Selamat datang", user)
    print("Informasi IDs:", IDs)
    print("Mata Kuliah yang diasistensi:", MK)

hubungkanSistem("asisten", "6", 
                nama = "Maulana", nim = "125090100111004",
                "MAB4137", "MAB4102"
                )
