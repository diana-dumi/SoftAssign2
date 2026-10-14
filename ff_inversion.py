from eea import eea
from long_division import *

def ff_inverse(f, p, h):

    if f == [0]:
        return None

    eea_list = eea(f, h, p)
    gcd = eea_list[2]


    if gcd != [1]:
        return None
    else:
        _, a = long_div(eea_list[0], h, p)
        return a