from sys import stdin


def check_answers(tests, answers):
    yes_ans = set(range(1, n + 1))
    no_ans = []
    for j in range(len(answers)):
        test = tests[j]
        answer = answers[j]
        t = map(int, test.split())
        if answer == 'YES':
            yes_ans &= set(t)
        else:
            no_ans += t

    return yes_ans, set(no_ans)


n = int(input())
i = 1
tests_list = []
answers_list = []
for line in stdin:
    txt_line = line.rstrip()
    if 'HELP' == txt_line:
        break
    if i % 2 == 0:
        answers_list.append(txt_line)
    else:
        tests_list.append(txt_line)
    i += 1

yes, no = check_answers(tests_list, answers_list)

# print('+', yes)
# print('-', no)

ans = list(yes - no)
print(*sorted(ans))
