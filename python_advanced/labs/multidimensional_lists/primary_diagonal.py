n = int(input())

matrix = []

for _ in range(n):
    data = list(map(int, input().split()))
    matrix.append(data)

diagonal_sum = 0

for row_index in range(n):
    for col_index in range(n):
        if col_index == row_index:
            diagonal_sum += matrix[*row_index][*col_index]
print(diagonal_sum)