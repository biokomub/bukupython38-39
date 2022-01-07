#membuat folder dengan os.mkdir()

import os
import traceback as tb  

folderBaru = r"E:\TESTING\FOLDER 1"

try:
    os.mkdir(folderBaru)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{folderBaru} telah dibuat!")
