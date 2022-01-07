#uji P olsen (ujipolsen.py)

def ujiPOlsen(POlsen_tanah):
    if (POlsen_tanah < 0) :
        return "Nilai P Olsen tidak boleh dibawah 0"
    elif ((POlsen_tanah >= 0) and (POlsen_tanah <1)):
        return "Kadar P Olsen tanah sangat rendah"
    elif ((POlsen_tanah >= 1) and (POlsen_tanah <=2)):
        return "Kadar P Olsen tanah rendah"
    elif ((POlsen_tanah > 2) and (POlsen_tanah <=3)):
        return "Kadar P Olsen tanah sedang"
    elif ((POlsen_tanah > 3) and (POlsen_tanah <=5)):
        return "Kadar P Olsen tanah tinggi"
    else:
        return "Kadar P Olsen tanah sangat tinggi"
