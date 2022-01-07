#membuat folder majemuk dengan pathlib.Path.mkdir()

from pathlib import Path
import traceback as tb  

folderBaru = r"E:\TESTING\FOLDER 2\SUBFOLDER 1\4\5\6"

try:
    folderPath = Path(folderBaru)
    folderPath.mkdir(parents = True) 
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{folderPath} telah dibuat!")
