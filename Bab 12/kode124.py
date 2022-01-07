from sayhello import sayhello

from datetime import datetime as dt
import time

def sleep10s():
    time.sleep(10) #sleep 10 detik

def main():
    id = input("Masukkan Nama: ")
    print(sayhello.hello(id))
    print("Sekarang: ", dt.now())
    print("Mulai sleep program 10 detik")
    sleep10s()
    print("Sleep program 10 detik selesai")
    print(sayhello.goodbye(id))
    print("Sekarang: ", dt.now()) 
    
if __name__ ==  "__main__":
    main()
