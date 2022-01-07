#update dictionary dengan metode update()
dictA = {'A': 1, 'B': 2} 
dictB = {'B': 100, 'C': 3}

#menggunakan metode update()
dictC = dictA.update(dictB)

#mencetak isi dictionary
print("Isi Dict A: " + str(dictA))
print("Isi Dict B: " + str(dictB))
print("Hasil Update :" + str(dictC))
