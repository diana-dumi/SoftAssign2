from poly_mod import poly_modulo
from poly_multiplication import poly_multiply

def ff_multiply(f, g, p, h):
    #first multiply the two polynomials
    product = poly_multiply(f,g,p)
    #reduce the result to be modulo h
    reduced = poly_modulo(product, h, p)

    return reduced