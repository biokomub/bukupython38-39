#memindah file ke Recycle Bin/Trash

from send2trash import send2trash
import traceback as tb

file = r"E:\TESTING\xxx.txt"

try:
    send2trash(file)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{file} telah dipindah ke Recyle Bin/Trash!")
