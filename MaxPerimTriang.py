def max_perimeter_triangle(S):
    
    S.sort(reverse=True)
    
    
    for i in range(len(S) - 2):
        
        if S[i] < S[i + 1] + S[i + 2]:
            
            return (S[i], S[i + 1], S[i + 2])
    
 
    return [-1]
