x1, y1 = (int(input()), int(input()))
x2, y2 = (int(input()), int(input()))

isBlack1 = (x1 % 2 == 0 and y1 % 2 == 0) or (x1 % 2 != 0 and y1 % 2 != 0)
isBlack2 = (x2 % 2 == 0 and y2 % 2 == 0) or (x2 % 2 != 0 and y2 % 2 != 0)

if (isBlack1 and isBlack2) or (not isBlack1 and not isBlack2):
    print('YES')
else:
    print('NO')