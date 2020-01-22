from sys import stdin

n = int(input())
all_nums = set(range(1, n + 1))
answers = []


def handle_yes(ans):
    global all_nums
    answers.append("YES")
    all_nums &= ans


def handle_no(ans):
    global all_nums
    answers.append("NO")
    all_nums -= ans


for line in stdin:
    if 'HELP' == line.rstrip():
        break
    message = set(map(int, line.rstrip().split()))
    try_msg = all_nums & message
    if len(all_nums) // 2 < len(try_msg):
        handle_yes(try_msg)
    else:
        handle_no(try_msg)

print(*answers, sep='\n')
print(*sorted(list(all_nums)))
