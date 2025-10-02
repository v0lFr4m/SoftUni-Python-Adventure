def is_valid(row_1 ,col_1 , row_2 , col_2 , rows_ , cols_):
    return  0 <= row_1 < rows_ and 0 <= col_1 <= cols_ and 0 <= row_2 < rows_ and 0 <= col_2 < cols_

rows, cols = list(map(int , input().split()))

matrix = [[str(x) for x in input().split()] for _ in range(rows)]


while (line:=input()) != 'END':
    command = line.split()
    if command[0] == 'swap' and len(command) == 5:
        row1, col1 , row2 , col2 = [int(x) for x in command[1:]]
        if is_valid(row1 , col1 , row2 ,col2, rows , cols):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2],matrix[row1][col1]
            [print(*row) for row in matrix]
        else:
            print('Invalid input!')
            continue
    else:
        print('Invalid input!')
        continue
