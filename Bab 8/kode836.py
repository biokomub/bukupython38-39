#menggabung dictionary dengan dict(D1, **D2)
dictA = {'A': 1, 'B': 2} 
dictB = {'B': 100, 'C': 3}

#menggunakan dict(D1, **D2)
dictC = dict(D1, **D2)

#mencetak isi dictionary
print("Isi Dict A: " + str(dictA))
print("Isi Dict B: " + str(dictB))
print("Hasil Gabungan :" + str(dictC))
