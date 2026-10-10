def remove_leading_zeros(f):
    # Remove leading zero coefficients
    while len(f) > 1 and f[-1] == 0:
        f.pop()
        
    return f

def long_div(f, g, p):
    # Long division of two polynomials, mod p
    # If g is the zero polynomial, division by 0 not possible
    if len(g) == 0:
        return None
    
    q = [0] * (len(f) - len(g) + 1)
    r = f[:]
    
    while len(r) >= len(g):
        shift = len(r) - len(g) # len(f) = deg(f) + 1, here we want deg(r) - deg(g)
        coef = (r[-1] * pow(g[-1], -1, p)) % p
        
        q[shift] = (q[shift] + coef) % p # q = q + coef * X^{shift}
        
        for i, gi in enumerate(g):
            r[i + shift] = (r[i + shift] - coef * gi) % p
            
        remove_leading_zeros(r)
        
    return remove_leading_zeros(q) or [0], r or [0]