class Tumbuhan(str): 
    def __new__(cls, nama, nama_latin):  
        print("Tumbuhan", nama, 
              "nama ilmiahnya", nama_latin + ".") 
        return super(Tumbuhan, cls).__new__(
            cls, (nama, nama_latin))      

tumb1 = Tumbuhan("Rumput Teki", "Cyperus rotundus")
tumb2 = Tumbuhan("Tebu", "Saccharum officinarum")
tumb3 = Tumbuhan("Padi", "Oryza sativa")
tumb4 = Tumbuhan("Jagung", "Zea mays")
