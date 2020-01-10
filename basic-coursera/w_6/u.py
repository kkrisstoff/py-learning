def counted_sort(sequence, count):
    """
    :param sequence: int[] = 0..count
    :param count: int
    :return: int[]
    """
    out = [0] * (count + 1)
    for item in sequence:
        out[item] += 1
    # for i in range(len(out)):
    #     if out[i] > 0:
    #         print((str(i) + ' ') * out[i], end='')
    return out[1:]
