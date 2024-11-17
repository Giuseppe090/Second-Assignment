def max_toys(S, G):
    
    G.sort()
    
    num_toys = 0
    total_spent = 0
    
    for price in G:
        if total_spent + price <= S:
            total_spent += price
            num_toys += 1
        else:
            break
            
    return num_toys

