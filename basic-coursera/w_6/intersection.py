# Intersection


def x_in_list(arr, el, j):
    while j < len(arr):
        if arr[j] > el:
            return False, j
        if arr[j] == el:
            return True, j
        j += 1
    return False, j


def Intersection(a, b):
    c = []
    i = 0
    j = 0
    while i < len(b):
        is_in, j = x_in_list(a, b[i], j)
        if is_in:
            c.append(b[i])
        i += 1
    return c


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(*Intersection(l1, l2))
