#bekerja dengan pathlib.Path.rglob()

from pathlib import Path
import traceback as tb

#tentukan direktori kerja
dirKerja = "E:\TESTING"

#temukan file berakhiran ".pdf" 
try:
    pathDir = Path(dirKerja)
    for namaFile in pathDir.rglob("*.pdf"):
        print(namaFile)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
