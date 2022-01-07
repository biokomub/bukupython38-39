class Burung(object):
    def bunyi(self):
        print("Burung berkicau.")
 
class Harimau(object):
    def bunyi(self):
        print("Harimau mengaum.")

class Anjing(object):
    def bunyi(self):
        print("Anjing menggongong.")
     
def func(obj):
    obj.bunyi()
  
hewan1 = Burung()
hewan2 = Harimau()
hewan3 = Anjing()
  
func(hewan1)
func(hewan2)
func(hewan3)
