from collections import deque

rows, cols = list(map(int , input().split()))

text = deque(input())

matrix = []

for index_row in range(rows):
    matrix.append([""] * cols)
    for index_col in range(cols):
        if index_row % 2 == 0:
            matrix[index_row][index_col] = text[0]
        else:
            matrix[index_row][-1 - index_col] = text[0]
        text.rotate(-1)

[print(*row, sep='') for row in matrix]