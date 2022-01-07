#uji C (ujikarbon.py)

def ujiC(C_tanah):
    if (C_tanah < 0) :
        return "Nilai C tidak boleh dibawah 0"
    elif ((C_tanah >= 0) and (C_tanah < 1)):
        return "Kadar C tanah sangat rendah"
    elif ((C_tanah >= 1) and (C_tanah <= 2)):
        return "Kadar C tanah rendah"
    elif ((C_tanah > 2) and (C_tanah <= 3)):
        return "Kadar C tanah sedang"
    elif ((C_tanah > 3) and (C_tanah <= 5)):
        return "Kadar C tanah tinggi"
    else:
        return "Kadar C tanah sangat tinggi"
