#operasi list
lst = [60, 80, 200, 250, 450]


print("Isi List")
print("Isi: " + str(lst))
print("Nilai Faktor")
print("A: " + str(lst[0]))
print("B: " + str(lst[1]))


print("Operasi Penugasan")
print("Penambahan: " + str(lst[0] + lst[1]))
print("Pengurangan: " + str(lst[0] - lst[1]))
print("Perkalian: " + str(lst[0] * lst[1]))
print("Pembagian: " + str(lst[0] / lst[1]))


print("Operasi Relasional")
print("Sama dengan: " + str(lst[0] == lst[1]))
print("Tidak sama dengan: " + str(lst[0] != lst[1]))
print("Lebih dari: " + str(lst[0] > lst[1]))

print("Kurang Dari: " + str(lst[0] < lst[1]))
print("Lebih dari sama dengan: " + str(lst[0] >= lst[1]))
print("Kurang dari sama dengan: " + str(lst[0] <= lst[1]))


print("Operasi Logika")
print("AND: " + str(lst[0] and lst[1]))
print("OR: " + str(lst[0] or lst[1]))
print("NOT Faktor A: " + str(not lst[0]))
print("NOT Faktor B: " + str(not lst[1]))
