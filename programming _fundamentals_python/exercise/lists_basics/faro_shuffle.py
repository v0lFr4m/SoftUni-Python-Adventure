card = input().split()
count_of_shuffles = int(input())

half = len(card) // 2

for shuffle in range(count_of_shuffles):
    final_list = []
    first_half = card[:half]
    second_half = card[half:]

    for index in range(half):
        final_list.append(first_half[index])
        final_list.append(second_half[index])

    card = final_list

print(card)