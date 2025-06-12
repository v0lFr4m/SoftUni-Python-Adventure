def sorted_nums(num):
    sorting_numbers = sorted(num)
    return sorting_numbers


sequence_of_numbers = input().split()
sequence_of_numbers_as_int = [int(num) for num in sequence_of_numbers]

print(sorted_nums(sequence_of_numbers_as_int))