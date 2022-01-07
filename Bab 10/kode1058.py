def generator(nilai_awal, jumlah_isi, step):

    nilai = nilai_awal
    while (((nilai_awal != None) or 
            (jumlah != None)) == True):
        nilai_isian = (yield nilai)
        if nilai_isian is None:
            nilai = nilai + step
        else:
            nilai = nilai_isian
    
    yield nilai

#program_utama
jml_isian = 10
obj_gen = generator(0, jml_isian, 1)

batas = jml_isian    
for i in range(batas):   
    print(obj_gen.__next__())
        
obj_gen.close() 
