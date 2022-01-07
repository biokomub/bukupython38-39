class Tanaman(object):
    nama = "" 
    nama_latin = ""
    tipe_akar = "" 

    def __init__(self, nama, 
                 nama_latin, tipe_akar):    
        self.nama = nama
        self.nama_latin = nama_latin
        self.tipe_akar = tipe_akar
 
    def tampilData(self):
        
        def cekAkar():
            perakaran = ["tunggang", "serabut"]
            if (self.tipe_akar in perakaran) == True:
                if (self.tipe_akar == perakaran[0]):
                    print("Tanaman ini berakar tunggang.")
                    print("Tanaman ini adalah dikotil.")
                else:
                    print("Tanaman ini berakar serabut.")
                    print("Tanaman ini adalah monokotil.")
            else:
                print("Tipe akar ini tidak valid.")
            
        print("Tanaman ini bernama", self.nama + ".")
        print("Nama latinnya", self.nama_latin + ".")
        cekAkar()


tumb1 = Tanaman("Padi", 
                "Oryza sativa", 
                "serabut")

tumb2 = Tanaman("Kacang Tanah", 
                "Arachis hypogaea", 
                "tunggang")

tumb1.tampilData() 
tumb2.tampilData()  
