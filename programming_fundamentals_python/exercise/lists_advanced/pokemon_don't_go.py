sequence_of_numbers = list(map(int , input().split()))
sum_of_removed_elements = 0
while len(sequence_of_numbers) != 0:
    index_input = int(input())
    number = 0
    if 0 <= index_input < len(sequence_of_numbers):
        number = sequence_of_numbers.pop(index_input)
    elif 0 > index_input:
        num_to_add = sequence_of_numbers[-1]
        number = sequence_of_numbers[0]
        sequence_of_numbers[0] = sequence_of_numbers[-1]
    else:
        num_to_add = sequence_of_numbers[0]
        number = sequence_of_numbers[-1]
        sequence_of_numbers[-1] = sequence_of_numbers[0]
    sum_of_removed_elements += number

    for current_index, current_num in enumerate(sequence_of_numbers):
        if current_num <= number:
            sequence_of_numbers[current_index] += number
        else:
            sequence_of_numbers[current_index] -= number
print(sum_of_removed_elements)