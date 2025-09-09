import math


persons = int(input())
elevator_capacity_in_person = int(input())

course = math.ceil(persons / elevator_capacity_in_person)
print(course)