rows , cols = list(map(int, input().split()))
matrix = [input().split() for _ in range(rows)]

count = 0

for index_row in range(rows -1):
    for index_col in range(cols -1):
        if matrix[index_row][index_col] == matrix[index_row][index_col +1] == matrix[index_row +1][index_col] == matrix[index_row +1][index_col +1]:
            count += 1

print(count)