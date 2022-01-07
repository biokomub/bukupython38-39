#operasi tuple
tpl = (60, 80, 200, 250, 450)


print("Isi Tuple")
print("Isi: " + str(tpl))
print("Nilai Faktor")
print("A: " + str(tpl[0]))
print("B: " + str(tpl[1]))


print("Operasi Penugasan")
print("Penambahan: " + str(tpl[0] + tpl[1]))
print("Pengurangan: " + str(tpl[0] - tpl[1]))
print("Perkalian: " + str(tpl[0] * tpl[1]))
print("Pembagian: " + str(tpl[0] / tpl[1]))


print("Operasi Relasional")
print("Sama dengan: " + str(tpl[0] == tpl[1]))
print("Tidak sama dengan: " + str(tpl[0] != tpl[1]))
print("Lebih dari: " + str(tpl[0] > tpl[1]))

print("Kurang Dari: " + str(tpl[0] < tpl[1]))
print("Lebih dari sama dengan: " + str(tpl[0] >= tpl[1]))
print("Kurang dari sama dengan: " + str(tpl[0] <= tpl[1]))


print("Operasi Logika")
print("AND: " + str(tpl[0] and tpl[1]))
print("OR: " + str(tpl[0] or tpl[1]))
print("NOT Faktor A: " + str(not tpl[0]))
print("NOT Faktor B: " + str(not tpl[1]))
