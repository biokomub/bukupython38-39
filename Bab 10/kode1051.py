def decorator(fungsi):
    
    def halo(arg):
        print("Halo " + fungsi(arg) + ", apa kabar?")
    
    return halo

@decorator
def person(arg):
    return(arg)

person("Ginting")
