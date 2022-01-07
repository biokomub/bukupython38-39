#mengganti nama file

import os
import traceback as tb

fiLama = r"E:\TESTING\a.txt"
fiBaru = r"E:\TESTING\1.out"

try:
    os.rename(fiLama, fiBaru)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"Nama File telah diganti dari {fiLama} -> 
    {fiBaru}!")
