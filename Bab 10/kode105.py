def printDenganReturn():
    x = "Halo!"
    print(x)
    return x
  
def printDenganReturnTanpaNilai():
    x = "Halo!"
    print(x)
    return

def printTanpaReturn():
    x = "Halo!"
    print(x)

def main():
    ret = printDenganReturn()
    ret2 = printDenganReturnTanpaNilai()
    tanpa_ret = printTanpaReturn()

    print("Nilai yang dikembalikan")
    print("    Dengan Return: %s" % ret)
    print("    Dengan Return tanpa nilai: %s" % ret2)
    print("    Tanpa Return: %s" % tanpa_ret)

main()
