#menghapus folder

import shutil
import traceback as tb

folder = r"E:\TESTING\XXX"

try:
    shutil.rmtree(folder)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{folder} telah dihapus!")
