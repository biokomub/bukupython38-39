from multipledispatch import dispatch

@dispatch()
def fungsinama():
    print("Halo, saya fungsi!")    

@dispatch(str)
def fungsinama(arg1):
    print("Halo, saya", arg1)    

@dispatch(str, str)    
def fungsinama(arg1, arg2):
    print("Halo, saya", arg1, "dan ini", arg2)    

@dispatch(int, int)
def fungsinama(num1, num2):
    print("Halo, saya", num1, "dan ini", num2)   

#panggil fungsi
fungsinama()
fungsinama("Viol")
fungsinama("Samuel", "Putra")
fungsinama(1, 3)
