def multiplication_without_multiply(first: int, second: int, third: int):

    if first == 0 or second == 0 or third == 0:
        return 'zero'
    number_counter = 0
    if first < 0:
        number_counter += 1
    if second < 0:
        number_counter += 1
    if third < 0:
        number_counter += 1

    if number_counter == 1 or number_counter == 3:
        return 'negative'
    else:
        return 'positive'


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(multiplication_without_multiply(first_num, second_num, third_num))