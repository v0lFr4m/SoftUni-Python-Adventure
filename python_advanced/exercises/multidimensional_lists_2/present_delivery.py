presents = int(input())
size_of_neighborhood = int(input())
santa_pos = []
matrix = []
happy_kids = 0
gifted_kids = 0

directions = {'up':(-1, 0),
              'down': (1, 0),
              'left':(0, -1),
              'right':(0, 1)}


for row in range(size_of_neighborhood):
    matrix.append(input().split())
    for col in range(size_of_neighborhood):
        if matrix[row][col] == 'S':
            santa_pos = (row , col)
        elif matrix[row][col] == 'V':
            happy_kids += 1



while presents > 0:
    command = input()

    if command == 'Christmas morning':
        break

    next_row = santa_pos[0] + directions[command][0]
    next_col = santa_pos[1] + directions[command][1]

    if 0 <= next_row < size_of_neighborhood and 0 <= next_col < size_of_neighborhood:
        if matrix[next_row][next_col] == 'V':
            presents -= 1
            gifted_kids += 1
            matrix[next_row][next_col] = '-'

        elif matrix[next_row][next_col] == 'C':
            for direction in directions:
                next_r = next_row + directions[direction][0]
                next_c = next_col + directions[direction][1]

                if matrix[next_r][next_c] in 'VX' and presents > 0:
                    if matrix[next_r][next_c] == 'V':
                        gifted_kids += 1
                    presents -= 1
                matrix[next_r][next_c] = '-'

        matrix[santa_pos[0]][santa_pos[1]] = '-'
        santa_pos = [next_row, next_col]
        matrix[santa_pos[0]][santa_pos[1]] = 'S'
if presents == 0 and gifted_kids < happy_kids:
    print('Santa ran out of presents!')
for row in matrix:
    print(' '.join(row))

if gifted_kids == happy_kids:
    print(f'Good job, Santa! {happy_kids} happy nice kid/s.')
else:
    print(f'No presents for {happy_kids - gifted_kids} nice kid/s.')
