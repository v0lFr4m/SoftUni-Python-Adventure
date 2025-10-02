n = int(input())

matrix = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

searched_symbol = input()
position = None

for row_index in range(n):
    for col_index in range(n):
        if searched_symbol in matrix[row_index][col_index]:
            position = row_index,col_index
            print(position)
            exit()
print(f"{searched_symbol} does not occur in the matrix")