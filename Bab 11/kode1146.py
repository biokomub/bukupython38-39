class Burung(object):
    def bunyi(self):
        print("Burung berkicau.")
 
class Harimau(object):
    def bunyi(self):
        print("Harimau mengaum.")

class Anjing(object):
    def bunyi(self):
        print("Anjing menggongong.")
     
hewan1 = Burung()
hewan2 = Harimau()
hewan3 = Anjing()
for hewan in (hewan1, hewan2, hewan3):
    hewan.bunyi()
