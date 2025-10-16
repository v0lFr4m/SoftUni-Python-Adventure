MOVES = {'up':(-1, 0),'down': (1, 0),'left':(0, -1),'right':(0, 1)}
ENERGY = 15
NEEDED_NECTAR = 30
IS_RESTORED = False
size = int(input())

matrix = []
bee_pos =[0,0]
for row in range(size):
    matrix.append(list(input().strip()))
    for col in range(size):
        if matrix[row][col] == 'B':
            bee_pos = [row , col]
            matrix[row][col] = '-'


collected_nectar = 0

while True:
    if ENERGY <= 0:
        if collected_nectar >= NEEDED_NECTAR and not IS_RESTORED:
            ENERGY = collected_nectar - NEEDED_NECTAR
            collected_nectar = NEEDED_NECTAR
            IS_RESTORED = True
            if ENERGY <= 0:
                matrix[bee_pos[0]][bee_pos[1]] = 'B'
                print("This is the end! Beesy ran out of energy.")
                break
            continue
        else:
            matrix[bee_pos[0]][bee_pos[1]] = 'B'
            print("This is the end! Beesy ran out of energy.")
            break

    command = input()
    move = MOVES[command]
    current_row = bee_pos[0] + move[0]
    current_col = bee_pos[1] + move[1]
    # if out of the boundaries teleports bee to other side

    # version 1
    # current_row = (current_row + size) % size
    # current_col = (current_col + size) % size

    # version 2
    # if not (0 <= current_row < size and 0 <= current_col < size):
    #     current_row = (current_row + size) % size
    #     current_col = (current_col + size) % size
    #     bee_pos = [current_row, current_col]

    # version 3
    # if not (0 <= current_row < size and 0 <= current_col < size):
    #     if command == 'right':
    #         bee_pos = [current_row , current_col - size]
    #         current_row, current_col = bee_pos[0], bee_pos[1]
    #
    #     elif command == 'left':
    #         bee_pos = [current_row, current_col + size]
    #         current_row, current_col = bee_pos[0], bee_pos[1]
    #
    #     elif command == 'up':
    #         bee_pos = [current_row + size , bee_pos[1]]
    #         current_row , current_col = bee_pos[0],bee_pos[1]
    #
    #     elif command == 'down':
    #         bee_pos = [current_row - size , bee_pos[1]]
    #         current_row, current_col = bee_pos[0], bee_pos[1]


    # if steps of flower (number)
    if matrix[current_row][current_col].isdigit():
        collected_nectar += int(matrix[current_row][current_col])
        matrix[current_row][current_col] = '-'
        ENERGY -= 1
        bee_pos = [current_row, current_col]
        continue
    # set current pos of bee -1 energy
    bee_pos = [current_row , current_col]
    ENERGY -= 1

    # if reach the hive
    if matrix[current_row][current_col] == 'H':
        if collected_nectar < 30:
            print('Beesy did not manage to collect enough nectar.')
            matrix[current_row][current_col] = 'B'
            break
        else:
            matrix[current_row][current_col] = 'B'
            print(f"Great job, Beesy! The hive is full. Energy left: {ENERGY}")
            break

for row in matrix:
    print(*row, sep= '')










