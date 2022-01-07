#memindah file

import shutil
import traceback as tb 

sumber = r"E:\TESTING\Test Folder\a.txt"
tujuan = r"E:\TESTING\Backup\Backup Folder\a_.txt"

try:
    shutil.move(sumber, tujuan)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"File telah dipindah dari {sumber} ke {tujuan}!")
