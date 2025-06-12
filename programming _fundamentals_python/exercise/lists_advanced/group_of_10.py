sequence_of_numbers = list(map(int, input().split(', ')))

current_group = 0

max_group = max(sequence_of_numbers) // 10 + 1

if max(sequence_of_numbers) % 10 == 0:
    max_group -= 1

for groups in range(max_group):
    group_list = [num for num in sequence_of_numbers if current_group < num <= (current_group + 10)]
    current_group += 10
    print(f"Group of {current_group}'s: {group_list}")
    group_list.clear()