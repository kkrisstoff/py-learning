# Passing score
input_file = open("input.txt", 'r', encoding='utf-8')
out_file = open('output.txt', 'w', encoding='utf8')
MIN_SCORE = 40


def print_f(s):
    print(s, file=out_file)


students = list(input_file.readlines())
places = int(students.pop(0))

all_scores = []

for student in students:
    student = student.split()
    t_1 = int(student[-1])
    t_2 = int(student[-2])
    t_3 = int(student[-3])
    if t_1 < MIN_SCORE or t_2 < MIN_SCORE or t_3 < MIN_SCORE:
        continue
    all_scores.append((t_1 + t_2 + t_3))

input_file.close()

all_scores.sort(reverse=True)

if len(all_scores) <= places:
    min_score = 0
else:
    min_score = all_scores[places - 1]

if min_score == 0:
    print_f(0)
elif min_score == all_scores[places]:
    i = places
    while i > 0:
        if all_scores[i] > min_score:
            min_score = all_scores[i]
            break
        i -= 1
    if all_scores[0] == min_score:
        print_f(1)
    else:
        print_f(min_score)
else:
    print_f(min_score)

out_file.close()

# 3
# Кириллов Кирилл 80 84 35
# Евгенева Евгения 54 100 60
# Ильин Илья 92 99 69
# Викторова Виктория 66 77 67
