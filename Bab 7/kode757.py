#contoh mencetak string berpola dengan template string
from string import Template

nama = "Dollar"

t = Template("$$ adalah $nama!")
ts = t.substitute(nama=nama)

print(ts)
