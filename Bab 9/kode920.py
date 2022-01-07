#mengganti nama file

from pathlib import Path
import traceback as tb 

fiLama = r"E:\TESTING\a.txt"
fiBaru = r"E:\TESTING\1.out"

try:
    filePath = Path(fiLama)
    filePath.rename(fiBaru)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"File telah diganti dari {fiLama} \
    menjadi {fiBaru}!")
