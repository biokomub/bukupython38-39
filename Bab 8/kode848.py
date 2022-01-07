#operasi himpunan dengan frozenset
fzsA = frozenset({2, 3, 5, 7, 11, 13, 17, 19, 23})
fzsB = frozenset({1, 3, 5, 7, 9, 11, 13, 15, 17})

#mencetak isi frozenset
print("Isi fzs A: " + str(fzsA))
print("Isi fzs B: " + str(fzsB))

#operasi himpunan
a = fzsA.difference(fzsB) #selisih
b = fzsA.intersection(fzsB) #irisan
c = fzsA.symmetric_difference(fzsB) #beda setangkup
d = fzsA.union(fzsB)

print("Selisih fzs A dan fzs B: " + str(a))
print("Irisan fzs A dan fzs B: " + str(b))
print("Beda setangkup fzs A dan fzs B: " + str(c))
print("Gabungan fzs A dan fzs B: " + str(d))
