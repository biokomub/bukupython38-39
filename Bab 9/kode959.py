#pengarsipan dengan shutil.unpack_archive()

import shutil
import traceback as tb

#tentukan file diarsip yang akan dimekarkan
fileArsip = "E:\TESTING\Tugas Kuliah ZIP.zip"

#tentukan direktori tujuan pemekaran
tujuanMekar = "E:\TESTING\Tugas Kuliah ZIP Unpack"

#arsipkan file ke dalam zip
try:
    shutil.unpack_archive(fileArsip, tujuanMekar)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print("File", fileArsip, 
          "telah dimekarkan ke", tujuanMekar)
