#membuat dictionary kosong
dict1 = {}
print(dict1)

#menambah elemen pada dictionary
dict1[0] = 0
dict1[100] = 100
dict1[200] = 200
print(dict1) 

#mengambil nilai pada kunci 100
print(dict1[100])

#mengupdate nilai pada kunci 100, dari bernilai 100 -> 150
dict1[100] = 150
print(dict1)

#menghapus kunci 200
del dict1[200]
print(dict1)

#mengambil pasangan kunci-nilai dari dictionary
print(dict1.items())

#mengambil kunci yang ada di dictionary
print(dict1.keys())

#mengambil nilai yang ada di dictionary
print(dict1.values())
