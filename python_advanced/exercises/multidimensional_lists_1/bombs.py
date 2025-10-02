size_of_matrix = int(input())
matrix = []

for _ in range(size_of_matrix):
    row = list(map(int, input().split()))
    matrix.append(row)

bombs_input = input().split()
bombs = []

for b in bombs_input:
    r, c = map(int, b.split(','))
    bombs.append((r, c))

for row , col in bombs:
    value = matrix[row][col]
    if value <= 0:
        continue

    for b_row, b_col in bombs:
        bomb_value = matrix[b_row][b_col]
        if bomb_value <= 0:
            continue

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                n_row, n_col = b_row + dr, b_col + dc
                if n_row == b_row and n_col == b_col:
                    continue
                if 0 <= n_row < size_of_matrix and 0 <= n_col < size_of_matrix:
                    if matrix[n_row][n_col] > 0:
                        matrix[n_row][n_col] -= bomb_value

        matrix[b_row][b_col] = 0

    matrix[row][col] = 0

alive_cells = 0
sum_of_cells = 0

for row in matrix:
    for cell in row:
        if cell > 0:
            alive_cells += 1
            sum_of_cells += cell

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")

for row in matrix:
    print(' '.join(map(str, row)))
