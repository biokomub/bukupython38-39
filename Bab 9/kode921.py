#menghapus file

import os
import traceback as tb

file = r"E:\TESTING\xxx.txt"

try:
    os.remove(file)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{file} telah dihapus!")
