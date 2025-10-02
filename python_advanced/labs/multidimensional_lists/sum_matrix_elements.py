rows , cols = map(int,input().split(', '))

matrix = []
matrix_sum = 0
for _ in range(rows):
    data = list(map(int,input().split(', ')))
    matrix.append(data)
    matrix_sum += sum(data)

print(matrix_sum)
print(matrix)