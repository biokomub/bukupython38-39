#membuat list kosong
list1 = []
print(list1)

#menambah elemen pada list
list1.append(0)
list1.append(100)
list1.append(200)
print(list1) 

#mengambil indeks dari elemen list
print(list1.index(200))

#menyisipkan elemen pada list
list1.insert(1, 50)
print(list1)

#menghapus elemen pada list
list1.remove(50)
print(list1)

#membalik list
list1.reverse()
print(list1)

#mengambil indeks dari elemen list
print(list1.index(200))

#sortir list
list1.sort()
print(list1)

#sortir balik list 
list1.sort(reverse=True)
print(list1)

#mengupdate elemen 100 menjadi 1000
list1[1] = 1000
print(list1)
