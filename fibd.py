def conigli(mesi, vita):
    
    coppie = [0] * (mesi + 1)
    coppie[0] = 1  

    for mese in range(1, mesi + 1):
        if mese == 1:
            coppie[mese] = coppie[mese - 1]  
        else:
            
            coppie[mese] = coppie[mese - 1]
            if mese - vita - 1 >= 0:
                
                coppie[mese] -= coppie[mese - vita - 1]
            coppie[mese] += coppie[mese - 2]  

    return coppie[mesi]

