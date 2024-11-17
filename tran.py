def calcola_rapporto_transizione_trasversione(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Le due stringhe devono avere la stessa lunghezza.")

    transizioni = 0
    trasversioni = 0

    
    transizioni_basi = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}

    for base1, base2 in zip(s1, s2):
        if base1 != base2:
            if base1 in transizioni_basi and base2 == transizioni_basi[base1]:
                transizioni += 1
            else:
                trasversioni += 1

    
    if trasversioni == 0:
        
        return float('inf')  
    else:
        rapporto = transizioni / trasversioni
        return rapporto

