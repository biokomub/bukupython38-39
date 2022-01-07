def outer():

    def inner1():
        print("Inner 1")
        
    def inner2():
        print("Inner 2")

    return inner1()
    return inner2()
    
outer()    
