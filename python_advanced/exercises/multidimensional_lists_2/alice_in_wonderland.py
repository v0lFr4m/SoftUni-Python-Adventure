size_of_territory = int(input())

matrix = []
alice_pos = []

for row in range(size_of_territory):
    matrix.append(input().split())
    for col in range(size_of_territory):
        if matrix[row][col] == 'A':
            alice_pos = (row , col)
            matrix[row][col] = '*'

total_tea_bags = 0

possible_moves = {
    'up':(-1, 0),
    'down': (1, 0),
    'left':(0, -1),
    'right':(0, 1)}

while total_tea_bags < 10:
    current_direction = input()

    if current_direction not in possible_moves:
        continue

    move = possible_moves[current_direction]
    current_row = alice_pos[0] + move[0]
    current_col = alice_pos[1] + move[1]

    if not (0 <= current_row < size_of_territory and 0 <= current_col < size_of_territory):
        print("Alice didn't make it to the tea party.")
        break

    current_pos = matrix[current_row][current_col]
    if current_pos == 'R':
        matrix[current_row][current_col] = '*'
        print("Alice didn't make it to the tea party.")
        break

    elif current_pos.isdigit():
        total_tea_bags += int(current_pos)

    matrix[current_row][current_col] = '*'
    alice_pos = (current_row, current_col)

    if total_tea_bags >= 10:
        print('She did it! She went to the party.')
        break
for row in matrix:
    print(' '.join(row))
