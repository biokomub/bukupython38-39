from multipledispatch import dispatch

@dispatch()
def fungsinama():
    print("Halo, saya fungsi!")    

@dispatch(object)
def fungsinama(arg1):
    print("Halo, saya", arg1)    

@dispatch(object, object)    
def fungsinama(arg1, arg2):
    print("Halo, saya", arg1, "dan ini", arg2)    

@dispatch(object, object)
def fungsinama(num1, num2):
    print("Halo, saya", num1, "dan ini", num2)   

#panggil fungsi
fungsinama()
fungsinama("Viol")
fungsinama("Samuel", "Putra")
fungsinama(1, 3)
fungsinama("Maulana", 23) #campuran
fungsinama("Maulana", ["Biologi", "UB"]) #campuran
fungsinama("Maulana", ("Biologi", "UB")) #campuran
fungsinama("Maulana", {"1":"Biologi", "2":"UB"}) #campuran
