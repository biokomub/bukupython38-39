#uji C/N (cnratio.py)

def CNratio(CN_tanah):
    if (CN_tanah < 0) :
        return "Nilai N tidak boleh dibawah 0"
    elif ((CN_tanah >= 0) and (CN_tanah < 5)):
        return "Rasio C/N tanah sangat rendah"
    elif ((CN_tanah >= 5) and (CN_tanah <= 11)):
        return "Rasio C/N tanah rendah"
    elif ((CN_tanah > 11) and (CN_tanah <= 16)):
        return "Rasio C/N tanah sedang"
    elif ((CN_tanah > 16) and (CN_tanah <= 25)):
        return "Rasio C/N tanah tinggi"
    else:
        return "Rasio C/N tanah sangat tinggi"
