from long_division import *

def irred_check(f, p):
    # Check if a polynomial is irreducible over Z/pZ

    # If f has degree <= 1, it is irreducible
    if len(f) <= 2:
        return True 

    # Check for roots in Z/pZ
    for x in range(p):
        value = 0
        for i in range(len(f)):
            value += f[i] * (x ** i)
            value = value % p
        
        if value == 0:
            # f has a root in Z/pZ
            return False  

    if len(f) <= 4:
        # If f has degree <= 3 and no roots, it is irreducible
        return True

    # Since f has degree max 5, also check for factors of degree 2
    
    # Generate all monic polynomials of degree 2 over Z/pZ
    g = [0, 0, 1]

    for i in range(p):
        g[0] = i
        for j in range(p):
            g[1] = j
            
            q, r = long_div(f, g, p)
            if r == [0]:
                # g divides f
                return False

    # No roots and no factors found, thus irreducible
    return True  