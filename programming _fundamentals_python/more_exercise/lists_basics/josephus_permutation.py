circle_of_people_as_string = input().split()
number = int(input())
executed_number = []
circle_of_people_as_int = [int(man) for man in circle_of_people_as_string]


current_index = 0
while len(circle_of_people_as_int) > 0:
    if number > 0 :
        current_index = (current_index + number - 1) % len(circle_of_people_as_int)
        executed_number.append(circle_of_people_as_int[current_index])
        circle_of_people_as_int.pop(current_index)
    else:
        break

print(f"[{','.join(map(str, executed_number))}]")