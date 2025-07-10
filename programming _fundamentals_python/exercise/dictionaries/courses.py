courses = {}

while (line := input()) != 'end':
    course_name , student_name = line.split(" : ")
    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name] += [student_name]

for course_name, students in courses.items():
    print(f"{course_name}: {len(students)}")
    for student in students:
        print(f"-- {student}")