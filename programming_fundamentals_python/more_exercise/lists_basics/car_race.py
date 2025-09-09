sequence_of_numbers_as_string = input().split()

numbers_as_int = [int(num) for num in sequence_of_numbers_as_string]

half_index = len(numbers_as_int) // 2

left_time = 0
for i in range(half_index):
    if numbers_as_int[i] == 0:
        left_time *= 0.8
    left_time += numbers_as_int[i]

right_time = 0
for i in range(len(numbers_as_int) - 1, half_index, -1):
    if numbers_as_int[i] == 0:
        right_time *= 0.8
    right_time += numbers_as_int[i]
    

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")