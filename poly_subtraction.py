def poly_sub(f, g, p):
    # Subtraction of two polynomials, mod p
    h = []
        
    for i in range(min(len(f), len(g))):
        # Subtract every two coefficients with corresponding terms
        x = f[i] - g[i]
            
        # mod p
        x = x % p
                
        h.append(x)
            
    for i in range(min(len(f), len(g)), len(f)):
        # Append remaining coefficients of f, if deg(f) > deg(g)
        h.append(f[i])
            
    for i in range(min(len(f), len(g)), len(g)):
        # Subtract the remaining coefficients of g, if deg(g) > deg(f)
        # We consider the corresponding coefficient of f to be 0
        x = 0 - g[i]
            
        # mod p
        x = x % p
        
        h.append(x)
            
    return h