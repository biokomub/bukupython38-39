class Kucing(object):
    "Ini kelas kucing"
    def __init__(self): 
        pass  

    def bunyi(self):
        print("Meong!") 
    
class Anjing(object):
    "Ini kelas anjing"
    def __init__(self): 
        pass  

    def bunyi(self):
        print("Guk Guk!") 

class Macan(object):
    "Ini kelas macan"
    def __init__(self): 
        pass  

    def bunyi(self):
        print("Aaaauuuumm!") 

class Ayam(object):
    "Ini kelas ayam"
    def __init__(self): 
        pass  

    def bunyi(self):
        print("Kok kok petok!") 

def Berbunyi(obj):
    #ini akan melakukan dynamic dispatch
    #secara single dispatch
    #object obj yang dilewatkan bisa berupa instance
    #dari kelas buatan
    obj.bunyi()

seekorKucing = Kucing()
Berbunyi(Kucing)

seekorAnjing = Anjing()
Berbunyi(Anjing)

seekorMacan = Macan()
Berbunyi(Macan)

seekorAyam = Ayam()
Berbunyi(Ayam)
