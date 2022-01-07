#memindah folder

import shutil
import traceback as tb    

sumber = r"E:\TESTING\Test"
tujuan = r"E:\TESTING\Test Folder\Test Pindah"

try:
    shutil.move(sumber, tujuan)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"Folder telah dipindah dari {sumber} ke \
    {tujuan}!")
