size = int(input())
player_pos = [0, 0]
matrix = []
collected_stars = 2
for index_row in range(size):
    matrix.append(input().split())
    for index_col in range(size):
        if matrix[index_row][index_col] == 'P':
            player_pos = [index_row , index_col]
            matrix[index_row][index_col] = '.'

moves = {
    'up':(-1, 0),
    'down': (1, 0),
    'left':(0, -1),
    'right':(0, 1)}

while True:
    if collected_stars >= 10:
        print(f"You won! You have collected {collected_stars} stars.")
        break

    if collected_stars == 0:
        print("Game over! You are out of any stars.")
        break

    current_direction = input()
    move = moves[current_direction]

    current_row = player_pos[0] + move[0]
    current_col = player_pos[1] + move[1]

    if not (0 <= current_row < size and 0 <= current_col < size):
        current_row , current_col = 0 , 0

    if matrix[current_row][current_col] == '#':
        collected_stars -= 1
        continue

    player_pos = [current_row, current_col]

    if matrix[current_row][current_col] == '*':
        collected_stars += 1
        matrix[current_row][current_col] = '.'

matrix[player_pos[0]][player_pos[1]] = 'P'

print(f"Your final position is {player_pos}")
for row in matrix:
    print(' '.join(row))