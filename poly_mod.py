from long_division import *

def remove_leading_zeros(f):
    # Remove leading zero coefficients
    while f and f[-1] == 0:
        f.pop()
        
    return f

def poly_mod(f, h, p):
    # Reduce f modulo h, with coefficients mod p

    # bring every coefficient into [0, p-1]
    f = [c % p for c in f]

    # remove the zeros at the end
    f = remove_leading_zeros(f)

    # divide by h and keep only the remainder
    q, r = long_div(f, h, p)

    # the zero polynomial must be [0], not []
    if r == []:
        r = [0]

    return r