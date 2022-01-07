# variable scope

# ini variabel global
var = 69

#definisikan fungsi
def fungsiScope():
    global var
    var = 96
    return var
    
print("Isi variabel di luar fungsi: ", var)
print("Isi variabel di dalam fungsi: ", fungsiScope())
print("Isi variabel di luar fungsi sekarang: ", var)
