#menghapus file dengan aman

from secure_delete import secure_delete
import traceback as tb

folder = r"E:\TESTING\RAHASIA"

try:
    secure_delete.secure_random_seed_init()
    secure_delete.secure_delete(folder)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{folder} telah dihapus dengan aman!")
