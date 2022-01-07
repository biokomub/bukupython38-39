#bekerja dengan glob.iglob() dengan rekursi

import glob
import traceback as tb

#temukan file mengandung ".pdf" 
try:
    for namaFile in glob.iglob("**/*.pdf", 
                               recursive=True):
        print(namaFile)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
