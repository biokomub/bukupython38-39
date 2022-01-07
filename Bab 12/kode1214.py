#program uji tanah

import ujikimiatanah.ujikarbon as uC
import ujikimiatanah.ujinitrogen as uN
import ujikimiatanah.cnratio as uCN
import ujikimiatanah.ujikbebas as uK

import ujikimiatanah.ujiP.ujiptotal as uPT
import ujikimiatanah.ujiP.ujipbray as uPB
import ujikimiatanah.ujiP.ujipolsen as uPO

print("+++++++++++++++++++++++++++++++++++++++++")
print("Program Uji Tanah")
print("Silakan masukkan angka hasil uji")
print("+++++++++++++++++++++++++++++++++++++++++")

uji1 = float(input("Input nilai C tanah (%): "))
uji2 = float(input("Input nilai N tanah (%): "))
uji3 = uji1/uji2
uji4 = float(input("Input nilai P Total tanah (mg/100 g): "))
uji5 = float(input("Input nilai P Bray tanah (ppm P): "))
uji6 = float(input("Input nilai P Olsen tanah (ppm P): "))
uji7 = float(input("Input nilai K Bebas tanah (me/100 g): "))

a = uC.ujiC(uji1)
b = uN.ujiN(uji2)
c = uCN.CNratio(uji3)
d = uPT.ujiPtotal(uji4)
e = uPB.ujiPBray(uji5)
f = uPO.ujiPOlsen(uji6)
g = uK.ujiK(uji7)

print("+++++++++++++++++++++++++++++++++++++++++")
print("Laporan Hasil Uji")
print("+++++++++++++++++++++++++++++++++++++++++")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
