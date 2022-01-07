#membuat folder dengan pathlib.Path.mkdir()

from pathlib import Path
import traceback as tb  

folderBaru = r"E:\TESTING\FOLDER 2"

try:
    folderPath = Path(folderBaru)
    folderPath.mkdir() 
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{folderPath} telah dibuat!")
