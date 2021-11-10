#contoh mencetak string berpola dengan template string
from string import Template
a = "Arfan"

t = Template("Hallo semuanya, saya $nama!")
ts = t.substitute(nama=a)

print(ts)
