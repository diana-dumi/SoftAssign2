def multiplication(f, g, p):
    # Multiplication of two polinomials, mod p
    # Result will have degree at most len(f) + len(g) - 1
    h = [0] * (len(f) + len(g) - 1)
    
    for i1, j1 in enumerate(f):
        for i2, j2 in enumerate(g):
            h[i1 + i2] = (h[i1 + i2] + j1 * j2) % p

    return h