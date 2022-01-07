#uji K bebas (ujikbebas.py)

def ujiK(K_tanah):
    if (K_tanah < 0) :
        return "Nilai K tidak boleh dibawah 0"
    elif ((K_tanah >= 0) and (K_tanah < 0.1)):
        return "Kadar K bebas tanah sangat rendah"
    elif ((K_tanah >= 0.1) and (K_tanah <= 0.4)):
        return "Kadar K bebas tanah rendah"
    elif ((K_tanah > 0.4) and (K_tanah <= 0.6)):
        return "Kadar K bebas tanah sedang"
    elif ((K_tanah > 0.6) and (K_tanah <= 1.0)):
        return "Kadar K bebas tanah tinggi"
    else:
        return "Kadar K bebas tanah sangat tinggi"
