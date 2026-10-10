from poly_subtraction import *
from long_division import *

def ff_sub(f, g, p, h):
    # Subtraction of two polynomials in a finite field, mod p and mod h

    # Subtract the polynomials mod p
    diff_poly = poly_sub(f, g, p)

    diff_poly = remove_leading_zeros(diff_poly)

    if (len(f) < len(h)) and (len(g) < len(h)):
        # If the degree of the difference is less than the degree of h, we can return the difference
        return diff_poly
    
    # Reduce mod h
    _, reduced_poly = long_div(diff_poly, h, p)
    return reduced_poly