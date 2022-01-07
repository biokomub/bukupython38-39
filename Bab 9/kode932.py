#mengganti nama folder

from pathlib import Path
import traceback as tb 

foLama = r"E:\TESTING\UJI"
foBaru = r"E:\TESTING\GANTI NAMA"

try:
    foPath = Path(foLama)
    foPath.rename(foBaru)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"File telah diganti dari {foLama} \
          menjadi {foBaru}!")
