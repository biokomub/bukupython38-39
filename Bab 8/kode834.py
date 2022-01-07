#menggabung dictionary dengan metode unpacking
dictA = {'A': 1, 'B': 2} 
dictB = {'B': 100, 'C': 3}

#menggunakan unpacking
dictC = {**dictA,**dictB}

#mencetak isi dictionary
print("Isi Dict A: " + str(dictA))
print("Isi Dict B: " + str(dictB))
print("Hasil Gabungan :" + str(dictC))
