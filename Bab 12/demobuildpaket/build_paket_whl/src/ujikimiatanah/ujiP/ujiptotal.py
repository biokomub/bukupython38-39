#uji P total (ujiptotal.py)

def ujiPtotal(Ptot_tanah):
    if (Ptot_tanah < 0) :
        return "Nilai P total tidak boleh dibawah 0"
    elif ((Ptot_tanah >= 0) and (Ptot_tanah < 15)):
        return "Kadar P total tanah sangat rendah"
    elif ((Ptot_tanah >= 15) and (Ptot_tanah <= 21)):
        return "Kadar P total tanah rendah"
    elif ((Ptot_tanah > 21) and (Ptot_tanah <= 41)):
        return "Kadar P total tanah sedang"
    elif ((Ptot_tanah > 41) and (Ptot_tanah <= 60)):
        return "Kadar P total tanah tinggi"
    else:
        return "Kadar P total tanah sangat tinggi"
    
