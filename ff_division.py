from ff_inversion import ff_inverse
from ff_multiplication import ff_multiply

def ff_divide(f, g, p, h):
    # f/g is the same as f*g^(-1)

    inverse = ff_inverse(g, p, h)

    if inverse is None:
        return None

    multiplication = ff_multiply(f, inverse, p, h)

    return multiplication