#membuat folder majemuk dengan os.mkdir()

import os
import traceback as tb  
folderBaru = r"E:\TESTING\FOLDER 1\SUBFOLDER 1\1\2\3"

try:
    os.makedirs(folderBaru)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{folderPath} telah dibuat!")
