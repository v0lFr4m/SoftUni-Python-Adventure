students = {}

pair_of_rows = int(input())
for student in range(0,pair_of_rows):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = [grade]

    else:
        students[student_name] += [grade]

for student, grades in students.items():
    average = sum(grades) / len(grades)
    if average >= 4.50:
        print(f"{student} -> {average:.2f}")