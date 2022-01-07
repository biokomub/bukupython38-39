def remove_List(list):
    list.remove(0)

list = [0]
print("List sebelum dihapus nilainya: ", list)
print("Alamat List sebelum dihapus nilainya: ",
      id(list))
remove_List(list)
print("List sesudah dihapus nilainya: ", list)
print("Alamat List sesudah dihapus nilainya: ",
      id(list))
