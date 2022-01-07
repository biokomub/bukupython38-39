def outer():

    def inner1():
        print("Inner 1")
        
    return inner1()

outer()    
