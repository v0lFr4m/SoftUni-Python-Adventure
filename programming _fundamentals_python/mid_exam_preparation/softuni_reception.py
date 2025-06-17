first_employee_students = int(input())
second_employee_students = int(input())
third_employee_students = int(input())
students_count = int(input())
x = 0
answers_per_hour = first_employee_students + second_employee_students + third_employee_students
time_needed = 0
while students_count > 0:
    students_count -= answers_per_hour
    x += answers_per_hour
    time_needed += 1
    if time_needed % 4 == 0:
        time_needed += 1
print(f'Time needed: {time_needed}h.')