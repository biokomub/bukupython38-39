class KelasA(object): 
    def __init__(self): 
        pass

#buat objek    
KelasA = object() #membuat objek KelasA

#cek instance
if ((isinstance(KelasA, object)) == True):
    betul = "Ya"
    print("Apakah KelasA instance dari object? :", betul) 
else:
    betul = "Tidak"
    print("Apakah KelasA instance dari object? :", betul)
