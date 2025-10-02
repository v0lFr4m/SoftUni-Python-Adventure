def add(row , col , value , current_matrix):
    if 0 <= row < (len(matrix)) and 0 <= col <= (len(matrix[row])):
        current_matrix[row][col] += value
    else:
        print("Invalid coordinates")

def subtrack(row , col , value , current_matrix):
    if 0 <= row < (len(matrix) - 1) and 0 <= col <= (len(matrix[row]) - 1):
        current_matrix[row][col] -= value
    else:
        print("Invalid coordinates")

n_rows = int(input())

matrix = []
for _ in range(n_rows):
    data = list(map(int , input().split()))
    matrix.append(data)

while (line := input()) != 'END':
    command = line.split()
    action , current_row , current_col , current_value = command[0], int(command[1]), int(command[2]), int(command[3])
    if action == 'Add':
        add(current_row, current_col, current_value, matrix)


    elif action == 'Subtract':
        subtrack(current_row, current_col, current_value, matrix)

for row in matrix:
    print(" ".join(map(str, row)))