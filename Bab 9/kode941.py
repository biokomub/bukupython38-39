#memfilter hasil directory listing dari os.listdir()

import os
import traceback as tb

folder = r"E:\TESTING"

try:
    ListDir = os.listdir(folder)
    for entri in ListDir:
        #listing file
        if os.path.isfile(os.path.join(folder, entri)):
            print("File :", entri)
        #listing folder
        if os.path.isdir(os.path.join(folder, entri)):
            print("Subfolder :", entri)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
