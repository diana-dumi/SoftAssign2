from ff_multiplication import ff_multiply

# needed for the power function
def power(f, e, p, h):
    # f^e in the finite field, using square-and-multiply
    result = [1]
    base = f
    while e > 0:
        if e % 2 == 1:
            result = ff_multiply(result, base, p, h)
        base = ff_multiply(base, base, p, h)
        e = e // 2
    return result


def prime_divisors(N):
    # returns the list of distinct prime divisors of N
    primes = []
    d = 2
    while d * d <= N:
        if N % d == 0:      
            primes.append(d)
            while N % d == 0: 
                N = N // d
        d = d + 1
    if N > 1:       
        primes.append(N)
    return primes


def primitivity_check(f, p, h):
    # the zero polynomial is never primitive
    if f == [0]:
        return False

    # order of the field: q = p^n, with n = deg(h)
    n = len(h) - 1
    q = p ** n

    # prime divisors p_1, ..., p_k of q - 1
    primes = prime_divisors(q - 1)

    # Step 1
    i = 0                           
    k = len(primes)

    # Step 2: while a^((q-1)/p_i) != 1 and i <= k
    while i < k and power(f, (q - 1) // primes[i], p, h) != [1]:
        i = i + 1

    # Step 3: if i <= k output false, else true
    if i < k:
        return False
    else:
        return True