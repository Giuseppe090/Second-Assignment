def calcola_consensus_e_profile_matrix(sequenze):

    lunghezza = len(sequenze[0])
    num_sequenze = len(sequenze)

    profile_matrix = {'A': [0] * lunghezza,'C': [0] * lunghezza,'G': [0] * lunghezza,'T': [0] * lunghezza}
    

    
    for sequenza in sequenze:
        for i in range(lunghezza):
            nucleotide = sequenza[i]
            profile_matrix[nucleotide][i] += 1

    
    consensus_string = ""
    for i in range(lunghezza):
        max_count = 0
        max_nucleotide = ''
        for nucleotide in 'ACGT':
            if profile_matrix[nucleotide][i] > max_count:
                max_count = profile_matrix[nucleotide][i]
                max_nucleotide = nucleotide
        consensus_string += max_nucleotide

    return consensus_string, profile_matrix

