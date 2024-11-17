def trova_lunga_sottostringa_comune(genoma1, genoma2, genoma3):
    len1, len2, len3 = len(genoma1), len(genoma2), len(genoma3)

    
    dp = [[[0] * (len3 + 1) for _ in range(len2 + 1)] for __ in range(len1 + 1)]

    max_len = 0  
    ending_index = 0  

    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            for k in range(1, len3 + 1):
                if genoma1[i - 1] == genoma2[j - 1] == genoma3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                    if dp[i][j][k] > max_len:
                        max_len = dp[i][j][k]
                        ending_index = i  

    
    sottostringa_comune = genoma1[ending_index - max_len: ending_index]

    return sottostringa_comune
