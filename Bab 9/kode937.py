#memindah folder ke Recycle Bin/Trash

from send2trash import send2trash
import traceback as tb

folder = r"E:\TESTING\SAMPAH"

try:
    send2trash(folder)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{folder} telah dipindah ke Recyle Bin/Trash!")
