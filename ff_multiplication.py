from long_division import *
from poly_multiplication import poly_multiply

def ff_multiply(f, g, p, h):
    #first multiply the two polynomials
    product = poly_multiply(f,g,p)
    #reduce the result to be modulo h
    _, reduced = long_div(product, h, p)

    return reduced