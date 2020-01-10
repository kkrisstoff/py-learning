# Civil Defence
# TODO: Test 5 Time Limit Exceeded
n = int(input())
tws = list(map(int, input().split()))
towns = []
for i in range(n):
    towns.append((i + 1, tws[i]))
towns.sort(key=lambda point: point[1])

m = int(input())
shlts = list(map(int, input().split()))
shelters = []
for i in range(m):
    shelters.append((i + 1, shlts[i]))
shelters.sort(key=lambda point: point[1])

i = 0
length = len(shelters)


def get_nearest(curr_town):
    global shelters
    global i
    while i < len(shelters):
        nearest = shelters[0]
        if shelters[i][1] > curr_town:
            if abs(curr_town - shelters[i][1])\
                    < abs(curr_town - shelters[i - 1][1]):
                nearest = shelters[i]
            else:
                nearest = shelters[i - 1]
            break
        i += 1
    # shelters = shelters[i-1:]
    return nearest[0]
    # arr = list(map(lambda x: (x[0], abs(curr_town - x[1])), shelters))
    # nearest = min(arr, key=lambda x: x[1])
    # return nearest[0]


nearest_shelters = []
for town in towns:
    x_town = town[1]
    nearest_shelters.append((town[0], get_nearest(x_town)))

print(*list(map(lambda x: x[1], sorted(nearest_shelters))))
