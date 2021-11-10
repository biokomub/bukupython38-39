#contoh penanganan kesalahan yang tidak tepat

num = "5"
numB = None

try:
    numB = (num+1) * 2
except BaseException as e:
    print('Error: ', e)

print(numB)
