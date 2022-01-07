#menggabung dictionary dengan fungsi ChainMap()
from collections import ChainMap  

dictA = {'A': 1, 'B': 2} 
dictB = {'B': 100, 'C': 3}

#menggunakan ChainMap()
dictC = ChainMap(dictA, dictB)

#mencetak isi dictionary
print("Isi Dict A: " + str(dictA))
print("Isi Dict B: " + str(dictB))
print("Hasil ChainMap Gabungan :" + str(dictC))
print("Hasil Dict Gabungan :" + str(dict(dictC)))
