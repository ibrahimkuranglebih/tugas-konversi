def konversi_suhu(nilai, dari, ke) : 
    dari = dari.lower()
    ke = ke.lower()
    
    if dari not in ['c','f','k'] or ke not in ['c','f','k']:
        return "Satuan tidak valid. Gunakan 'C', 'F', atau 'K'."

    if dari == 'k' and nilai < 0:
        return "Nilai suhu dalam Kelvin tidak boleh negatif."
    if dari == "c" and (ke == "k" and (nilai + 273.15) < 0):
        return "Error: Hasil Kelvin tidak boleh negatif."
    if dari == "f" and (ke == "k" and ((nilai - 32) * 5/9 + 273.15) < 0):
        return "Error: Hasil Kelvin tidak boleh negatif."
    
    if dari == ke:
        return nilai
    
    hasil = None
    #celcius
    if dari == 'c':
        if ke == 'f':
            hasil = (nilai *(9/5)) + 32
        elif ke == 'k':
            hasil = nilai + 273.15
    #farenheit        
    elif dari == 'f':
        if ke == 'c':
            hasil = (nilai - 32) * (5/9)
        elif ke == 'k':
            hasil = (nilai - 32) * (5/9) + 273.15
    #kelvin
    elif dari == 'k':
        if ke == 'c':
            hasil = nilai - 273.15
        elif ke == 'f':
            hasil = (nilai - 273.15) * 9/5 + 32
            
    return hasil
