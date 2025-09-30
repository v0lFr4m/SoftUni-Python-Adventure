number_of_students = int(input())
data = {}

for student in range(number_of_students):
    student_name, grade = input().split()
    if student_name not in data:
        data[student_name] = [float(grade)]
    else:
        data[student_name] += [float(grade)]


for student, grade in data.items():
    print(f"{student} -> {' '.join([f'{el:.2f}'for el in grade])} (avg: {sum(grade) / len(grade):.2f})")

