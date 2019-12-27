# point (x, y)
# circle (xc, yc, r)
def IsPointInCircle(x, y, xc, yc, r):
    x_ = abs(x - xc)
    y_ = abs(y - yc)
    return (x_ ** 2 + y_ ** 2) ** 0.5 <= r


def fast_pow(x, n):
    if n % 2 == 0:
        return (x ** 2) ** (n / 2)
    else:
        return x * fast_pow(x, n - 1)


def MinDivisor(n):
    i = 2
    while i < int(n ** 0.5) + 1:
        if n % i == 0:
            return i
        i += 1
    return n


# The Euclidean Algorithm
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# Have no idea what is it,
# but the tests were passed
def C(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    if k == n:
        return 1
    return C(n - 1, k) + C(n - 1, k - 1)
