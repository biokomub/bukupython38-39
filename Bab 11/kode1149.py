from abc import ABCMeta, abstractmethod

class Hewan(metaclass = ABCMeta):
    def narasi(self):
        print("Ada banyak hewan.", 
              "Setiap hewan berbunyi,", 
              "dengan caranya sendiri.")
    @abstractmethod
    def bunyi(self):
        pass
        
class Burung(Hewan):
    def bunyi(self):
        print("Burung berkicau.")
 
class Harimau(Hewan):
    def bunyi(self):
        print("Harimau mengaum.")

class Anjing(Hewan):
    def bunyi(self):
        print("Anjing menggongong.")
     
hewan1 = Burung()
hewan2 = Harimau()
hewan3 = Anjing()
for hewan in (hewan1, hewan2, hewan3):
    hewan.narasi()
    hewan.bunyi()
