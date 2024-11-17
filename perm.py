from itertools import permutations

def genera_permutazioni(n):
    if n < 1 or n > 7:
        raise ValueError("Il numero deve essere compreso tra 1 e 7.")

    
    numeri = list(range(1, n + 1))
    
    
    permutazioni = list(permutations(numeri))
    
    
    print(len(permutazioni))
    
    
    for perm in permutazioni:
        print(" ".join(map(str, perm)))
