def min_max_and_sum(numbers):
    sum_numbers = 0
    for num in numbers:
        sum_numbers += num
    return print(f"The minimum number is {min(numbers)}\nThe maximum number is {max(numbers)}\nThe sum number is: {sum_numbers}\n")

numbers_as_string = input().split()
numbers_as_int = [int(num) for num in numbers_as_string]

min_max_and_sum(numbers_as_int)