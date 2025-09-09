import math

number_of_students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendance = 0
total_student_attendance = []
for student in range(number_of_students):
    attendance = int(input())

    if lectures > 0:
        total_bonus = attendance / lectures * (5 + additional_bonus)
    else:
        total_bonus = 0

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendance = attendance

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")

