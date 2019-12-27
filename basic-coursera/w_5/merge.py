

# TODO
# don't use sort methods
def merge(a, b):
    new_list = a + b

    # i = int(len(new_list)/2) + 1
    # while i < 0:
    #     # sort list

    return new_list


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(merge(l1, l2))
