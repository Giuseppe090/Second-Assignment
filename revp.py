def reverse_complement(seq):
    """Restituisce il reverse complement di una sequenza di DNA."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

def trova_reverse_palindrome(dna_sequence):
    """Trova tutte le reverse palindrome in una sequenza di DNA di lunghezza superiore a 4."""
    reverse_palindromes = []

    
    for length in range(4, len(dna_sequence) + 1):  
        for start in range(len(dna_sequence) - length + 1):
            subseq = dna_sequence[start:start + length]
            if subseq == reverse_complement(subseq):
                reverse_palindromes.append((start + 1, length))  

    return reverse_palindromes
