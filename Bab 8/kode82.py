#mengimpor pustaka array
import array

#membuat objek array bertipe integer
objArray = array.array('i')
print(objArray)

#mengidentifikasi tipe array
print(objArray.typecode)

#menambah elemen pada array
objArray.append(0)
objArray.append(100)
objArray.append(200)
print(objArray) 

#mengambil indeks dari elemen array
print(objArray.index(200))

#menyisipkan elemen pada array
objArray.insert(1, 50)
print(objArray)

#menghapus elemen pada array
objArray.remove(50)
print(objArray)

#membalik array
objArray.reverse()
print(objArray)

#mengambil indeks dari elemen array
print(objArray.index(200))
