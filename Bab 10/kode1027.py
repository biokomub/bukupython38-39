def update_List(list):
    list[0] = 1

list = [0]
print("List sebelum diperbaharui: ", list)
print("Alamat List sebelum diperbaharui: ", id(list))
update_List(list)
print("List sesudah diperbaharui: ", list)
print("Alamat List sesudah diperbaharui: ", id(list))
