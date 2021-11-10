#contoh mencetak string berpola dengan template string
from string import Template

t = Template("Hallo, saya $nama dari angkatan $akt!")
ts = t.substitute(nama="Bayu", akt=2014)

print(ts)
