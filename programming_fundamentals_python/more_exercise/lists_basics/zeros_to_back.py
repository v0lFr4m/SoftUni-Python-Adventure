numbers_as_string = input().split(", ")

numbers_as_int = [int(num) for num in numbers_as_string]

for zero in numbers_as_int:
    if zero == 0:
        numbers_as_int.remove(zero)
        numbers_as_int.append(zero)
print(numbers_as_int)
