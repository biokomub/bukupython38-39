#bekerja dengan glob.iglob()

import glob
import traceback as tb

#temukan file mengandung ".pdf" 
try:
    for namaFile in glob.iglob("*.pdf"):
        print(namaFile)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
