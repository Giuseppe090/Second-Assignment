codoni = {'A': ['GCT', 'GCC', 'GCA', 'GCG'],
    'C': ['TGT', 'TGC'],
    'D': ['GAT', 'GAC'],
    'E': ['GAA', 'GAG'],
    'F': ['TTT', 'TTC'],
    'G': ['GGT', 'GGC', 'GGA', 'GGG'],
    'H': ['CAT', 'CAC'],
    'I': ['ATT', 'ATC', 'ATA'],
    'K': ['AAA', 'AAG'],
    'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'M': ['ATG'],
    'N': ['AAT', 'AAC'],
    'P': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Q': ['CAA', 'CAG'],
    'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'T': ['ACT', 'ACC', 'ACA', 'ACG'],
    'V': ['GTT', 'GTC', 'GTA', 'GTG'],
    'W': ['TGG'],
    'Y': ['TAT', 'TAC'],
    'STOP': ['TAA', 'TAG', 'TGA']}

def conta_stringhe_dna(proteina):
    numero_stringhe = 1  
    for aminoacido in proteina:
        if aminoacido in codoni:
            numero_stringhe *= len(codoni[aminoacido])
        else:
            print(f"Aminoacido sconosciuto: {aminoacido}")
            return 0  
    return numero_stringhe

################################ NdG: Secondo me l'indicazione input-output in questo esercizio di Rosalind è sbagliata.
################################ Contando manualmente si vede bene che le stringhe RNA da cui le proteine MA potrebbero
################################ essere state tradotte sono 4, non 12. Almeno a me sembra così 