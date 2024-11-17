def count_rna_strings(protein):
    # Codon map for each amino acid
    codon_map = {
        'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'STOP': 3,
        'C': 2, 'W': 1, 'P': 4, 'H': 2, 'Q': 2,
        'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2,
        'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2,
        'G': 4
    }
    
    total_combinations = 1
    
    # Iterate through each amino acid in the protein string
    for amino_acid in protein:
        if amino_acid in codon_map:
            total_combinations *= codon_map[amino_acid]
        else:
            return 0  # If an unknown amino acid is found, return 0
    
    return total_combinations

# Example usage
protein_string = "MA"
result = count_rna_strings(protein_string)
print(f"Il numero totale di stringhe di RNA da cui la stringa di proteine '{protein_string}' potrebbe essere stata tradotta è: {result}")