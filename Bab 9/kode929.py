#mengkopi folder

import shutil
import traceback as tb

sumber = r"E:\TESTING\Folder Asli\",
tujuan = r"E:\TESTING\Test Folder\Folder Kopi"

try:
    shutil.copytree(sumber, tujuan)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{sumber} telah dikopi ke {tujuan}!")
