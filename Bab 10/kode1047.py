def outer():

    def inner1(func):
        func()
        
    def inner2():
        print("Inner 2")

    inner1()

outer()    
