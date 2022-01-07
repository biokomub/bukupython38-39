#membuat kelas Pizza
class Pizza(object):
    "Ini adalah Kelas pembuat objek pizza"
    #inisiasi pembuatan pizza dan atributnya
    def __init__(self, jenis, lebar, 
                 tebal, irisan, crust, *topping):
        self.jenis = jenis
        self.lebar = lebar
        self.tebal = tebal
        self.irisan = irisan
        self.topping = tuple(topping)
        self.crust = crust
    
    #tampilkan sajian pizza    
    def SajikanPizza(self):
        "Ini metode untuk menyajikan Pizza"
        #olah topping    
        def daftarTopping(*args):
            "ini metode internal untuk\
                mengolah topping Pizza"
            args = self.topping
            Topping = []
              [Topping.append(x) for x in args if x not in Topping]
            return tuple(Topping)
        
        #cetak penyajian
        print("Ini Pizza", self.jenis + "." + 
              " Lebarnya", (str(self.lebar)) + " cm." + 
              " Tebalnya", (str(self.tebal)) + " cm." +
              " Diiris", (str(self.irisan)) + " bagian." +
              " Crustnya", self.crust + ".", end = "")
              
        print("\nToppingnya: ")
        p = daftarTopping()
        if ((p != tuple()) and (p[0] != "")):
            for index, item in enumerate(p):
                if index is not ((len(p)-1)):
                    print(item, end = ", ", )
                else:
                    print("dan", item, end = "")
        elif ((p != tuple()) and (p[0] == "")):
            for index, item in enumerate(p):
                if index is not ((len(p)-1)):
                    print("Mana Toppingnya?", 
                          "Pizza ini Tidak ada toppingnya", 
                          end = "")
                else:
                    print("Mana Toppingnya?", 
                          "Pizza ini Tidak ada toppingnya", 
                          end = "")
        else:
            print("Mana Toppingnya?", 
                  "Pizza ini Tidak ada toppingnya",
                  end = "")            

        print("\nSaya suka pizza ini.")

#buat objek pizzaku        
Pizzaku = Pizza("Pizza Pepperoni", 30, 0.3, 8, 
                "tebal", "Pepperoni", "Keju Mozarella")
#tampilkan sajian pizza
Pizzaku.SajikanPizza()
