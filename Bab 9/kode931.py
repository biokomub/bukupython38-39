#mengganti nama folder

import os
import traceback as tb

foLama = r"E:\TESTING\UJI"
foBaru = r"E:\TESTING\GANTI NAMA"

try:
    os.rename(foLama, foBaru)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"Nama Folder telah diganti dari {foLama} \
    menjadi {foBaru}!")
