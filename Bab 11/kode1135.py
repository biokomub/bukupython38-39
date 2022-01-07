class KelasA(object): 
    def __init__(self): 
        pass

#buat objek    
objA = KelasA() #membuat objek objA

#cek instance
if ((isinstance(objA, KelasA)) == True):
    betul = "Ya"
    print("Apakah objA instance dari KelasA? :", betul) 
else:
    betul = "Tidak"
    print("Apakah objA instance dari KelasA? :", betul)
