def print_ans(is_true):
    if is_true:
        print('YES')
    else:
        print('NO')


def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n - 1)


def average(arr):
    """
    :param arr: int[]
    :return: float
    """
    if len(arr) == 0 or sum(arr) == 0:
        return 0
    return sum(arr)/len(arr)
