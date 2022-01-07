#uji N (ujinitrogen.py)

def ujiN(N_tanah):
    if (N_tanah < 0) :
        return "Nilai N tidak boleh dibawah 0"
    elif ((N_tanah >= 0) and (N_tanah < 0.1)):
        return "Kadar N tanah sangat rendah"
    elif ((N_tanah >= 0.1) and (N_tanah <= 0.21)):
        return "Kadar N tanah rendah"
    elif ((N_tanah > 0.21) and (N_tanah <= 0.51)):
        return "Kadar N tanah sedang"
    elif ((N_tanah > 0.51) and (N_tanah <= 0.75)):
        return "Kadar N tanah tinggi"
    else:
        return "Kadar N tanah sangat tinggi"
    
