def tambah_ke_List(list):
  list.append(1)

list = [0]
print("List sebelum ditambah: ", list)
print("Alamat List sebelum ditambah: ", id(list))
tambah_ke_List(list)
print("List sesudah ditambah: ", list)
print("Alamat List sesudah ditambah: ", id(list))
