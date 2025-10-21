MOVES = {'up':(-1, 0),'down': (1, 0),'left':(0, -1),'right':(0, 1)}
ARMOR = 300
size = int(input())
enemy_count = 0
jet_pos = [0,0]

matrix = []
for row_index in range(size):
    matrix.append(list(input().strip()))
    for col_index in range(size):
        if matrix[row_index][col_index] == 'J':
            jet_pos = [row_index ,col_index]
            matrix[row_index][col_index] = '-'
        elif matrix[row_index][col_index] == 'E':
            enemy_count += 1

while ARMOR != 0 and enemy_count != 0:
    command = input()

    direction = MOVES[command]

    current_row = jet_pos[0] + direction[0]
    current_col = jet_pos[1] + direction[1]

    if not (0 <= current_row < size and 0 <= current_col < size):
        break


    if matrix[current_row][current_col] == 'E':
        matrix[current_row][current_col] = '-'
        enemy_count -= 1
        if enemy_count != 0:
            ARMOR -= 100
        else:
            jet_pos = [current_row, current_col]
            print("Mission accomplished, you neutralized the aerial threat!")
            break

    if matrix[current_row][current_col] == 'R':
        ARMOR = 300
        matrix[current_row][current_col] = '-'

    jet_pos = [current_row ,current_col]
    matrix[jet_pos[0]][jet_pos[1]] = '-'
matrix[jet_pos[0]][jet_pos[1]] = 'J'
if ARMOR == 0:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates {[jet_pos[0], jet_pos[1]]}!")
for row in matrix:
    print(*row, sep= '')