#uji P bray (ujipbray.py)

def ujiPBray(PBray_tanah):
    if (PBray_tanah < 0) :
        return "Nilai P Bray tidak boleh dibawah 0"
    elif ((PBray_tanah >= 0) and (PBray_tanah < 5)):
        return "Kadar P Bray tanah sangat rendah"
    elif ((PBray_tanah >= 5) and (PBray_tanah <= 8)):
        return "Kadar P Bray tanah rendah"
    elif ((PBray_tanah > 8) and (PBray_tanah <= 11)):
        return "Kadar P Bray tanah sedang"
    elif ((PBray_tanah > 11) and (PBray_tanah <= 15)):
        return "Kadar P Bray tanah tinggi"
    else:
        return "Kadar P Bray tanah sangat tinggi"
    
