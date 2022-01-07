def outer():
    def inner1(func):
        def inner1A():
            return inner2()
        inner1A()
        
    def inner2():
        print("Inner 2")

    return inner1(inner2)
    
outer()    
