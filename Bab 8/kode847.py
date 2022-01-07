#operasi himpunan dengan set
setA = set({2, 3, 5, 7, 11, 13, 17, 19, 23})
setB = set({1, 3, 5, 7, 9, 11, 13, 15, 17})

#mencetak isi set
print("Isi set A: " + str(setA))
print("Isi set B: " + str(setB))

#operasi himpunan
a = setA.difference(setB) #selisih
b = setA.intersection(setB) #irisan
c = setA.symmetric_difference(setB) #beda setangkup
d = setA.union(setB)

print("Selisih set A dan set B: " + str(a))
print("Irisan set A dan set B: " + str(b))
print("Beda setangkup set A dan set B: " + str(c))
print("Gabungan set A dan set B: " + str(d))
