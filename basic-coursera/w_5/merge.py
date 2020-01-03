# merge
# don't use sort methods
# TODO: Test 13: Time Limit Exceeded


def push_in_place(i_list, el):
    i = 0
    for l_el in i_list:
        if int(l_el) > int(el):
            break
        i += 1
    i_list.insert(i, el)
    return i_list


def merge(a, b):
    for b_el in b:
        push_in_place(a, b_el)
    return a


l1 = list(input().split())
l2 = list(input().split())
print(*merge(l1, l2))
