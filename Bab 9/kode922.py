#menghapus file

from pathlib import Path
import traceback as tb

file = r"E:\TESTING\xxx.txt"
try:
    filePath = Path(file)
    filePath.unlink()
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{file} telah dihapus!")
