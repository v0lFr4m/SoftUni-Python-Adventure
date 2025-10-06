
SIZE = 5
matrix = []
player_pos = []
targets = 0

for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == 'A':
            player_pos = (row , col)
        elif matrix[row][col] == 'x':
            targets += 1

shot_targets = []
directions = {
    'up':(-1, 0),
    'down': (1, 0),
    'left':(0, -1),
    'right':(0, 1)}


for _ in range(int(input())):
    command = input().split()
    action = command[0]
    direction = command[1]
    move = directions[direction]

    if command[0] == 'shoot':
        current_row = player_pos[0] + move[0]
        current_col = player_pos[1] + move[1]

        while 0 <= current_row < SIZE and 0 <= current_col < SIZE:
            if matrix[current_row][current_col] == 'x':
                shot_targets.append([current_row,current_col])
                matrix[current_row][current_col] = '.'
                targets -= 1
                break

            current_row += move[0]
            current_col += move[1]

        if targets == 0:
            print(f"Training completed! All {len(shot_targets)} targets hit.")
            break


    elif action == "move":
        steps = int(command[2])
        current_row = player_pos[0] + move[0] * steps
        current_col = player_pos[1] + move[1] * steps
        if 0 <= current_row < SIZE and 0 <= current_col < SIZE and matrix[current_row][current_col] == '.':
            player_pos = [current_row, current_col]


if targets >0:
    print(f'Training not completed! {targets} targets left.')
[print(row) for row in shot_targets]


