#menghapus folder

from pathlib import Path
import traceback as tb

folder = r"E:\TESTING\XXX"

try:
    folderPath = Path(folder)
    folderPath.rmdir()
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{folderPath} telah dihapus!")
