# val of N
def fib_n(n):
    if n < 1:
        return n
    i = 1
    prev = 0
    curr = 1
    while i < n:
        prev, curr = curr, curr + prev
        i += 1
    return curr


# is X in Fibonacci Sequence
def x_in_fib_1(x):
    if x < 1:
        return x
    i = 1
    prev = 0
    curr = 1
    while curr <= x:
        prev, curr = curr, curr + prev
        i += 1
        if x == curr:
            return i
    return -1


# TODO: use recursion
def x_in_fib_2(x):
    if x < 1:
        return x
    i = 1
    prev = 0
    curr = 1
    while curr <= x:
        prev, curr = curr, curr + prev
        i += 1
        if x == curr:
            return i

    return -1
