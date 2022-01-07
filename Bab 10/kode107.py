#contoh penggunaan lambda untuk filter()

umur = [11, 15, 17, 23, 26, 38, 51]

#filter untuk membuat list baru hasil filter
hasil_filter = list(filter(lambda x: (x < 17), umur))
print(hasil_filter)
