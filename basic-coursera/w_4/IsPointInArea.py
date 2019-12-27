# TODO: Haven't been passed yet :(
def IsPointInCircle(x, y, xc, yc, r):
    x_ = abs(x - xc)
    y_ = abs(y - yc)

    return (x_ ** 2 + y_ ** 2) ** 0.5 <= r


def IsPointBetweenLines(x, y):
    if y > 0:
        return x / y >= -1 and (y - 2 * x) <= 2
    else:
        return x / y <= -1 and (y - 2 * x) >= 2


def IsPointInArea(x, y):
    print(IsPointInCircle(x, y, -1, -1, 2))
    print(IsPointBetweenLines(x, y))
    if y > 0:
        return IsPointInCircle(x, y, -1, -1, 2) and IsPointBetweenLines(x, y)
    else:
        return (not IsPointInCircle(x, y, -1, -1, 2)) and IsPointBetweenLines(x, y)


if IsPointInArea(float(input()), float(input())):
    print('YES')
else:
    print('NO')
