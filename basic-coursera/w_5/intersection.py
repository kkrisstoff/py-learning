

# TODO: Test 15: Time Limit Exceeded
def x_in_list(el, arr):
    for a_el in arr:
        if el == a_el:
            return True
    return False


def Intersection(a, b):
    c = []
    for b_el in b:
        # cnt = a.count(b_el)
        # if cnt > 0:
        #     c.append(b_el)
        if x_in_list(b_el, a):
            c.append(b_el)

    return c


l1 = list(input().split())
l2 = list(input().split())
print(*Intersection(l1, l2))
