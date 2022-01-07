class Pembulatan(float): 
    def __new__(cls, angka, ndigit):  
        return super(Pembulatan, cls).__new__(
            cls,(round(angka, ndigit)))

class PenjumlahanBulat(int): 
    def __new__(cls, angka1, angka2):  
        return super(Penjumlahan, cls).__new__(
            cls,(angka1 + angka2))

a = 1.2345
print("Hasil pembulatan", a, "adalah", Pembulatan(a, 2))

b = 2
c = 5
print("Hasil penjumlahan bulat", b, "dan", c,
      "adalah", PenjumlahanBulat(b, c))
