rows , cols = map(int, input().split(', '))

matrix = []

for _ in range(rows):
    data = list(map(int, input().split()))
    matrix.append(data)

for col_index in range(cols):
    col_sum = 0
    for row_index in range(rows):
        col_sum += matrix[row_index][col_index]
    print(col_sum)
