class KelasA(object): 
    def __init__(self): 
        pass

#cek instance
if ((issubclass(KelasA, object)) == True):
    betul = "Ya"
    print("Apakah KelasA subkelas dari object? :", betul) 
else:
    betul = "Tidak"
    print("Apakah KelasA subkelas dari object? :", betul)
