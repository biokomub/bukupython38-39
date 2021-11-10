#contoh mencetak string berpola dengan template string
from string import Template

dict = {"nama" : "Bayu", "akt" : 2014}

t = Template("Hallo, saya $nama dari angkatan $akt!")
ts = t.substitute(**dict)

print(ts)
