import random
from long_division import remove_leading_zeros
from ff_prim_check import *

def random_element(p, h):
    # generate random element of Zp[X]/(h): polynomial of degree < deg(h)
    n = len(h) - 1
    f = [random.randint(0, p - 1) for _ in range(n)]
    return remove_leading_zeros(f)

def primitive_element(p, h):
    # Step 1
    a = random_element(p, h)
    # Step 2: while a is not primitive, pick another random element
    while not primitivity_check(a, p, h):
        a = random_element(p, h)
    # Step 3
    return a