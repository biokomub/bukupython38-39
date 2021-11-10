#contoh pendayagunaan raise 

INVALID_NUM_EXCEPTION = Exception("Harus integer!")

num = "5"

if type(num) != int:
    raise INVALID_NUM_EXCEPTION
    print (num+1)*2
