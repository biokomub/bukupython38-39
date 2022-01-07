def outer():

    def inner1():
        print("Inner 1")
        
    def inner2():
        print("Inner 2")

    inner1()
    inner2()
    
outer()    
