def decorator(fungsi):
    
    def halo(*args, **kwargs): 
        b = fungsi(*args, **kwargs) 
        print("Halo " , str(b) , ", apa kabar?")
    
    return halo

@decorator
def person(arg):
    return(arg)

#melewatkan string
person(("Maulana, Bayu"))

#melewatkan tuple berisi string
person(("Maulana", "Bayu"))

#melewatkan tuple berisi angka
person(("177013", "265918"))

#melewatkan dictionary
person({"key1":"Maulana", "key2":"Bayu"})
