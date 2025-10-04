size_of_field = int(input())

matrix = []
bunny_pos = []
egs = []
for row in range(size_of_field):
    matrix.append(input().split())
    for col in range(size_of_field):
        if matrix[row][col] == 'B':
            bunny_pos = [row , col]

max_eggs = float('-inf')
max_direction = ''
max_eggs_pos = []

possible_moves = {'up':(-1, 0), 'down': (1, 0), 'left':(0, -1), 'right':(0, 1)}

for direction, move in possible_moves.items():
    eggs = 0
    current_egg_pos = []
    current_row = bunny_pos[0] + move[0]
    current_col = bunny_pos[1] + move[1]
    while 0 <= current_row < size_of_field and 0 <= current_col < size_of_field:
        if matrix[current_row][current_col] == 'X':
            break
        eggs += int(matrix[current_row][current_col])
        current_egg_pos.append([current_row, current_col])

        current_row += move[0]
        current_col += move[1]

    if eggs > max_eggs and current_egg_pos:
         max_eggs = eggs
         max_eggs_pos = current_egg_pos
         max_direction = direction

print(max_direction)
[print(row) for row in max_eggs_pos]
print(max_eggs)


