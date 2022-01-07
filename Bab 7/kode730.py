# padding akan kehilangan fungsi bila menerima 
# ukuran angka lebih besar dari padding yang disediakan 
print("{:5d}".format(1234))
print("{:5d}".format(12345))
print("{:5d}".format(123456))

# hal yang sama terjadi juga di float  
print("{:5f}".format(12345))
print("{:5f}".format(123456))
