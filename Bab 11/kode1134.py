class KelasA(object): 
    def __init__(self): 
        pass

#buat objek    
objA = KelasA() #membuat objek objA

#cek instance apakah objA instance dari object
if ((isinstance(objA, object)) == True):
    betul = "Ya"
    print("Apakah objA instance dari object? :", betul) 
else:
    betul = "Tidak"
    print("Apakah objA instance dari object? :", betul) 
