def sort_dict(d):
    sorted_dict = {}
    for k in sorted(d):
        sorted_dict[k] = d[k]

    return sorted_dict


def sort_dic_by_val(d):
    return sorted(
        d.items(),
        key=lambda x: x[1],
        reverse=True
    )
