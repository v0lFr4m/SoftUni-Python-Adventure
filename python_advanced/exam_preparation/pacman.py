MOVES = {'up':(-1, 0),'down': (1, 0),'left':(0, -1),'right':(0, 1)}

size = int(input())
stars = 0
matrix = []
health = 100
packman_pos = [0,0]
for row in range(size):
    matrix.append(list(input().strip()))
    for col in range(size):
        if matrix[row][col] == "P":
            packman_pos = [row , col]
            matrix[row][col] = "-"
        if matrix[row][col] == "*":
            stars += 1

SHIELD = False


while health > 0 and stars > 0:
    command = input()
    if command == 'end':
        break

    direction = MOVES[command]

    current_row = packman_pos[0] + direction[0]
    current_col = packman_pos[1] + direction[1]

    if not (0 <= current_row < size and 0 <= current_col < size):
        current_row = (current_row + size) % size
        current_col = (current_col + size) % size
        packman_pos = [current_row, current_col]

    if matrix[current_row][current_col] == 'F':
        SHIELD = True
        matrix[current_row][current_col] = "-"
        continue


    elif matrix[current_row][current_col] == '*':
        stars -= 1
        matrix[current_row][current_col] = "-"

    elif matrix[current_row][current_col] == "G":
        if SHIELD:
            matrix[current_row][current_col] = "-"
            packman_pos = [current_row, current_col]
            SHIELD = False
            continue
        else:
            health -= 50
            matrix[current_row][current_col] = "-"
    packman_pos = [current_row , current_col]
    matrix[current_row][current_col] = '-'

matrix[packman_pos[0]][packman_pos[1]] = 'P'

if health == 0:
    print(f"Game over! Pacman last coordinates [{packman_pos[0]},{packman_pos[1]}]")
elif stars == 0:
    print("Pacman wins! All the stars are collected.")
elif health > 0 and stars > 0:
    print("Pacman failed to collect all the stars.")
print(f"Health: {health}")
if stars != 0:
    print(f"Uncollected stars: {stars}")

for row in matrix:
    print(''.join(row))