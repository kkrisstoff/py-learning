# Civil Defence

n = int(input())
towns = list(input().split())
for i_t in range(n):
    towns[i_t] = [int(towns[i_t]), i_t + 1, 0]
towns.sort()

m = int(input())
shelters = list(input().split())
for i_sh in range(m):
    shelters[i_sh] = [int(shelters[i_sh]), i_sh + 1]
shelters.sort()

i = 0
for town in towns:
    # arr = list(map(lambda x: abs(town[0] - x[0]), shelters))
    # min_pos = arr.index(min(arr))
    # shelters = shelters[min_pos:]

    """
    town = (len, id, shelterId)
    shelter = (len, id)
    """
    curr_town = town[0]
    if shelters[0][0] >= curr_town:
        town[2] = shelters[0][1]
        continue
    if shelters[len(shelters) - 1][0] <= curr_town:
        town[2] = shelters[len(shelters) - 1][1]
        continue
    while i < len(shelters):
        if shelters[i][0] > curr_town:
            if abs(curr_town - shelters[i - 1][0])\
                    < abs(curr_town - shelters[i][0]):
                town[2] = shelters[i - 1][1]
            else:
                town[2] = shelters[i][1]
            break
        else:
            town[2] = shelters[i][1]
        i += 1

print(*map(lambda x: x[2], sorted(towns, key=lambda x: x[1])))
