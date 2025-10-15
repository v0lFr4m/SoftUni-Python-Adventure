size_of_field = int(input())
spaceship_pos = []
field = []
resources = 100
for row in range(size_of_field):
    field.append(input().split())
    for col in range(size_of_field):
        if field[row][col] == 'S':
            spaceship_pos = (row , col)
            field[row][col] = '.'

moves = {
    'up':(-1, 0),
    'down': (1, 0),
    'left':(0, -1),
    'right':(0, 1)}

while resources >= 5:
    current_direction = input()

    move = moves[current_direction]
    current_row = spaceship_pos[0] + move[0]
    current_col = spaceship_pos[1] + move[1]
    resources -= 5

    if not (0 <= current_row < size_of_field and 0 <= current_col < size_of_field):
        field[spaceship_pos[0]][spaceship_pos[1]] = 'S'
        print('Mission failed! The spaceship was lost in space.')
        break

    current_pos = field[current_row][current_col]
    # when reached planet
    if current_pos == 'P':
            print(f'Mission accomplished! The spaceship reached Planet B with {resources} resources left.')
            break

    # when reached meteorites
    elif current_pos == 'M':
        resources -= 5
        field[current_row][current_col] = '.'

    # when reached space station / refiling
    elif current_pos == 'R':
        resources += 10
        if resources > 100:
            resources = 100
        spaceship_pos = (current_row, current_col)
        continue

    field[current_row][current_col] = '.'
    spaceship_pos = (current_row, current_col)

    if resources < 5:
        field[current_row][current_col] = 'S'
        print(f'Mission failed! The spaceship was stranded in space.')
        break

if resources < 0:
    print("Mission failed! The spaceship was stranded in space.")
for row in field:
    print(' '.join(row))