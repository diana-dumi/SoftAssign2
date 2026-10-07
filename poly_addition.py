def poly_add(f, g, p):
    # Addition of two polynomials, mod p
    h = []
    
    for i in range(min(len(f), len(g))):
        # Add every two coefficients with corresponding terms
        x = f[i] + g[i]
        
        # mod p
        x = x % p
            
        h.append(x)
        
    for i in range(min(len(f), len(g)), len(f)):
        # Add remaining coefficients of f, if deg(f) > deg(g)
        h.append(f[i])
        
    for i in range(min(len(f), len(g)), len(g)):
        # Add remaining coefficients of g, if deg(g) > deg(f)
            h.append(g[i])
        
    return h