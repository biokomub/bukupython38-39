import sys 

if ('win32' not in sys.platform):
    raise AssertionError("Kode ini Windows-only.")
