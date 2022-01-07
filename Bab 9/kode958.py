#pengarsipan dengan shutil.make_archive()

import shutil
import traceback as tb

#tentukan direktori yang akan diarsip
dirArsip = "E:\TESTING\Tugas Kuliah"

#tentukan direktori dan file (tanpa ekstensi)
Tujuan = "E:\TESTING\Tugas Kuliah ZIP"

#arsipkan file ke dalam zip
try:
    zipfile = shutil.make_archive(Tujuan, "zip", dirArsip)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print("Arsip", zipfile, "telah dibuat!")    
