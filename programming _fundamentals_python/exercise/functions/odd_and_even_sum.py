def sum_of_odd_and_even_nums(single_string):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in single_string:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
single_num_as_string = input()

sum_of_odd_and_even_nums(single_num_as_string)


