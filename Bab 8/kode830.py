#operasi dictionary
dict =  {"A":60, "B": 80, "C": 200, "D": 250, "E": 450}


print("Isi Dictionary")
print("Isi: " + str(dict))
print("Nilai Faktor")
print("A: " + str(dict["A"]))
print("B: " + str(dict["B"]))


print("Operasi Penugasan")
print("Penambahan: " + str(dict["A"] + dict["B"]))
print("Pengurangan: " + str(dict["A"] - dict["B"]))
print("Perkalian: " + str(dict["A"] * dict["B"]))
print("Pembagian: " + str(dict["A"] / dict["B"]))


print("Operasi Relasional")
print("Sama dengan: " + str(dict["A"] == dict["B"]))
print("Tidak sama dengan: " + str(dict["A"] != dict["B"]))
print("Lebih dari: " + str(dict["A"] > dict["B"]))

print("Kurang Dari: " + str(dict["A"] < dict["B"]))
print("Lebih dari sama dengan: " + str(dict["A"] >= dict["B"]))
print("Kurang dari sama dengan: " + str(dict["A"] <= dict["B"]))


print("Operasi Logika")
print("AND: " + str(dict["A"] and dict["B"]))
print("OR: " + str(dict["A"] or dict["B"]))
print("NOT Faktor A: " + str(not dict["A"]))
print("NOT Faktor B: " + str(not dict["B"]))
