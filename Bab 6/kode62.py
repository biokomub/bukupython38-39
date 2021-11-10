A = int(input("masukkan pembilang: "))
B = int(input("masukkan penyebut: "))

if (B==0): 
    raise ZeroDivisionError

print(A/B)
