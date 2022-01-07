#bekerja dengan glob.glob() dengan rekursi

import glob
import traceback as tb

#temukan file mengandung ".pdf" 
try:
    for namaFile in glob.glob("**/*.pdf", 
                              recursive=True):
        print(namaFile)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
