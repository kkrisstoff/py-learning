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


def js_map(val_list, callback):
    """
    JS like map
    # def do_stuff(val, i):
    #   print(i, '=>', val)
    #   return i * 2
    # l2 = js_map(list(map(int, input().split())), do_stuff)
    # print(*l2)
    :param val_list: any[]
    :param callback: fn
    :return: any[]
    """
    index_list = range(len(val_list) + 1)
    return list(map(callback, val_list, index_list))
