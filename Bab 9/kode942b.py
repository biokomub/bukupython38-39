#memfilter hasil directory listing dari 
#pathlib.Path.iterdir()

from pathlib import Path 
import traceback as tb

folder = r"E:\TESTING"

try:
    DirPath = Path(folder)
    ListDir = DirPath.iterdir()
    for entri in ListDir:
        #listing file
        if entri.is_file():
            print("File :", entri.name)
            print("File Path :", entri)
        #listing folder
        if entri.is_dir():
            print("Subfolder :", entri.name)
            print("Subfolder Path :", entri)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
