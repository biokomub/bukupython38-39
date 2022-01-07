#memfilter hasil directory listing dari os.scandir()

import os
import traceback as tb

folder = r"E:\TESTING"

try:
    ListDir = os.scandir(folder)
    for entri in ListDir:
        #listing file
        if os.path.isfile(os.path.join(folder, entri)):
            print("File :", entri.name)
            print("File Path :", entri.path)
        #listing folder
        if os.path.isdir(os.path.join(folder, entri)):
            print("Subfolder :", entri.name)
            print("Subfolder Path :", entri.path)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
