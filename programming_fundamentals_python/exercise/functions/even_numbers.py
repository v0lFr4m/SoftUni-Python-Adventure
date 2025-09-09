def even(num):
    if num % 2 == 0:
        return True
sequence_of_nums = input().split()
sequence_of_nums_as_int = [int(num)for num in sequence_of_nums]

print(list(filter(even , sequence_of_nums_as_int)))
