from poly_subtraction import *
from poly_multiplication import *
from long_division import *

def eea(f, g, p):
    # Extended Euclidean algorithm of two polynomials, mod p
    f = remove_leading_zeros([c % p for c in f])
    g = remove_leading_zeros([c % p for c in g])
    
    # gcd(0, 0) is undefined
    if not f and not g:
        return None
    
    x = [1]
    v = [1]
    y = []
    u = []
    
    while len(g) > 0:
        q, r = long_div(f, g, p)
        
        f = g
        g = r
        
        xx = x
        yy = y
        x = u
        y = v
        
        u = remove_leading_zeros(poly_sub(xx, poly_multiply(q, u, p), p))
        v = remove_leading_zeros(poly_sub(yy, poly_multiply(q, v, p), p))
    
    # gcd is monic
    leading_coef_f = [pow(f[-1], -1, p)]
    
    a = remove_leading_zeros(poly_multiply(x, leading_coef_f, p))
    b = remove_leading_zeros(poly_multiply(y, leading_coef_f, p))
    gcd = remove_leading_zeros(poly_multiply(f, leading_coef_f, p))

    # The zero polynomial is [] internally, but return it as [0]
    return a or [0], b or [0], gcd or [0]