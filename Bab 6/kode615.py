#contoh penggunaan traceback

import traceback 

num = "5"
numB = None

try:
    numB = (num+1) * 2
except BaseException as e:
    e = traceback.format_exc()
    print('Error: ', e)

print(numB)
