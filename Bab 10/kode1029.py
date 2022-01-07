def reassign_List(list):
  list = [0, 1]

list = [0]
print("List sebelum direassign: ", list)
print("Alamat List sebelum direassign: ", id(list))
reassign_List(list)
print("List sesudah direassign: ", list)
print("Alamat List sesudah direassign: ", id(list))
