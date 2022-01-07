class KelasA(object): 
    def __init__(self): 
        pass

#cek instance
if ((isinstance(KelasA, object)) == True):
    betul = "Ya"
    print("Apakah KelasA instance dari object? :", betul) 
else:
    betul = "Tidak"
    print("Apakah KelasA instance dari object? :", betul)
