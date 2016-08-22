# non-recursive modular exponentiation
# source: http://www.math.umn.edu/~garrett/crypto/Code/FastPow_Python.html


def modXP(x, d, n):
    X = x
    D = d
    Y = 1
    while D > 0:
        if D % 2 == 0:
            X = (X * X) % n
            D /= 2
        else:
            Y = (X * Y) % n
            D -= 1
    return Y
