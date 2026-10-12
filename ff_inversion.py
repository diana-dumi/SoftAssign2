from eea import eea
from poly_mod import poly_modulo

def ff_inverse(f, p, h):

    if f == [0]:
        return None

    eea_list = eea(f, h, p)
    gcd = eea_list[2]


    if gcd != [1]:
        return None
    else:
        a = eea_list[0]
        return poly_modulo(a, h, p)