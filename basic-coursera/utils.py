def print_ans(is_true):
    if is_true:
        print('YES')
    else:
        print('NO')


def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n - 1)
