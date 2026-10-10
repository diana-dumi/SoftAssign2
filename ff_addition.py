from poly_addition import *
from long_division import *

def ff_add(f, g, p, h):
    # Addition of two polynomials in a finite field, mod p and mod h

    # Add the polynomials mod p
    sum_poly = poly_add(f, g, p)

    sum_poly = remove_leading_zeros(sum_poly)

    if (len(f) < len(h)) and (len(g) < len(h)):
        # If the degree of the sum is less than the degree of h, we can return the sum
        return sum_poly
    
    # Reduce mod h
    _, reduced_poly = long_div(sum_poly, h, p)
    return reduced_poly