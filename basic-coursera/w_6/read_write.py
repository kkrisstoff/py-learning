from os import path

script_dir = path.dirname(__file__)
file_path = path.join(script_dir, "input.txt")
input_file = open(file_path, 'r', encoding='utf-8')
# out_file = open('output.txt', 'w', encoding='utf8')

students = []
for line in input_file:
    data = line.split()
    students.append((int(data[2]), int(data[3])))
input_file.close()

students.sort()
classes = {
    9: [],
    10: [],
    11: []
}
for student in students:
    classes[student[0]].append(student[1])

m9 = max(classes[9])
m10 = max(classes[10])
m11 = max(classes[11])

print(
    classes[9].count(m9),
    classes[10].count(m10),
    classes[11].count(m11))
# for student in students:
#     print(*student, file=out_file)
# out_file.close()
