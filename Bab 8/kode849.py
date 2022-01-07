#operasi manipulasi set
setA = set({1, 2, 3, 4, 5})
print("Isi mula – mula set A: " + str(setA))

#tambahkan satu elemen baru, 10, ke set A
setA.add(10)
print("Isi set A sekarang setelah ditambah elemen baru: " + 
str(setA))

#perbaharui isi set A dengan set B
setB = set({100, 200})
setA.update(setB)
print("Isi set A sekarang setelah diperbaharui set B: " + 
str(setA))

#hapus elemen 3 pada set A
setA.remove(3)
print("Isi set A sekarang setelah 3 dihapus: " + str(setA))

#bersihkan setA
setA.clear()
print("Isi set A sekarang setelah dibersihkan: " + str(setA))
