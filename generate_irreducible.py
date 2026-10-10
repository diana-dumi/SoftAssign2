from irred_check import *

def gen_irred(n, p):
    # Generate a random irreducible polynomial of degree n over Z/pZ

    if n == 1:
        # Return a degree 1 polynomial
        return [1, 1]

    # There are p^n monic polynomials of degree n over Z/pZ, 
    total = p ** n

    for x in range(1, total):
        coef = [0] * n + [1] 
        m = x
        for i in range(n):
            coef[i] = m % p
            m //= p
        if irred_check(coef, p):
            return coef