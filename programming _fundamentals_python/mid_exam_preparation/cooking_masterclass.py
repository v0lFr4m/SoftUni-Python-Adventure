import math

budget = float(input())
students = int(input())
price_for_flour = float(input())
price_for_single_egg = float(input())
price_for_single_apron = float(input())
free_packages = 0
for student in range(1 , students + 1):
    if student % 5 == 0:
        free_packages += 1
    #1 package of flour, 10 eggs, and an apron.
apron = price_for_single_apron * (math.ceil(students + (students * 0.20)))
egg = price_for_single_egg * 10 * students
flour = price_for_flour * (students - free_packages)
total = apron + egg + flour


if total <= budget:
    print(f"Items purchased for {total:.2f}$.")
else:
    print(f"{abs(budget - total):.2f}$ more needed.")