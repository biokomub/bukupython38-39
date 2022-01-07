#menghapus file dengan aman

from secure_delete import secure_delete
import traceback as tb

file = r"E:\TESTING\xxx.txt"

try:
    secure_delete.secure_random_seed_init()
    secure_delete.secure_delete(file)
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    print(f"{file} telah dihapus dengan aman!")
