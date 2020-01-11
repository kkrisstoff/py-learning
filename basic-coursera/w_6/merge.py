# merge
# don't use sort methods


def merge(a, b):
    merged = []
    i = 0
    j = 0
    while i < len(b) or j < len(a):
        if i >= len(b):
            merged.append(a[j])
            j += 1
            continue
        if j >= len(a):
            merged.append(b[i])
            i += 1
            continue
        if b[i] < a[j]:
            merged.append(b[i])
            i += 1
        else:
            merged.append(a[j])
            j += 1

    return merged


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(*merge(l1, l2))
