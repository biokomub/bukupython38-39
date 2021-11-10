#contoh mencetak string berpola dengan template string
from string import Template
a = "Oky"
b = "2012" 

t = Template("Hallo, saya $nama dari angkatan $akt!")
ts = t.substitute(nama=a, akt=b)

print(ts)
