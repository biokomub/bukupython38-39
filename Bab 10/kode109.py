# membuat Fungsi Komposisi

# Fungsi untuk mengkombinasi 2 fungsi
def fungsi_komposisi(f, g):
    return lambda x : f(g(x))
  
# Fungsi 1
def fungsi_1(x):
    return (2*x) + 3
  
# Fungsi 2
def fungsi_2(x):
    return x + 1
  
# Fungsi Komposisi mengembalikan Fungsi Lambda
# Disini variabel fkomp menyimpan 
# lambda x : fungsi_1(fungsi_2(x))
fkomp = fungsi_komposisi(fungsi_1, fungsi_2)

# Input nilai variabel x disini
var = int(input("Masukkan nilai x: "))
print(fkomp(var))
