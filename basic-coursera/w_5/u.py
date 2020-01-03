# JS like map
# How to use:
# def do_stuff(val, i):
#     print(i, '=>', val)
#     return i * 2
# l2 = js_map(list(map(int, input().split())), do_stuff)
# print(l2)
def js_map(val_list, callback):
    index_list = range(len(val_list) + 1)
    return list(map(callback, val_list, index_list))
