def factorial(n):
    f = 1
    for i in range(1, n+1):
        f  = f *i
    return f

def combination(i, j):
    return factorial(i)/(factorial(j) * factorial(i - j))

def independent_alleles(k, n):
    print('Seconda legge di Mendel')
    print ("C'è un solo Tom nella 0a generazione. Ogni discendente avrà due figli e ciascun coniuge sarà AaBb. >")
    print('La probabilità che la kesima generazione sia AaBb è 0,25')
    p = 0
    count = pow(2, k)                       
    for i in range(n, count+1):
        p += combination(count, i) * pow(0.25, i) * pow(0.75, count - i)
    return p