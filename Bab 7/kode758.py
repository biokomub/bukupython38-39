#contoh mencetak string berpola dengan template string
from string import Template

dict = {"nama" : "Maulana", "prodi" : "Biologi",
        "univ_asal" : "Universitas Brawijaya",
        "akt" : 2012, "profesi" : "Mahasiswa Doktoral"}

t = Template("$nama adalah alumni $prodi $univ_asal \
angkatan $akt yang kini berprofesi $profesi sebagai \
di $tempat.")
ts = t.substitute(**dict)

print(ts)
