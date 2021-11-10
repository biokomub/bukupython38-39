#contoh raise

INVALID_NUM_EXCEPTION = Exception("Harus integer!")

num = "5"

assert isinstance(num, int), INVALID_NUM_EXCEPTION
print(num+1)*2
