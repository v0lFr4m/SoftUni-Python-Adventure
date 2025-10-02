rows , cols = list(map(int , input().split()))
max_sum = float('-inf')

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

sub_matrix = []
for index_row in range(rows -2):
    for index_col in range(cols -2):
        first_row = [matrix[index_row][index_col], matrix[index_row][index_col + 1], matrix[index_row][index_col + 2]]
        second_row = [matrix[index_row + 1][index_col], matrix[index_row + 1][index_col + 1], matrix[index_row + 1][index_col + 2]]
        third_row = [matrix[index_row + 2][index_col], matrix[index_row + 2][index_col + 1], matrix[index_row + 2][index_col + 2]]

        total_sum = sum(first_row + second_row + third_row)

        if total_sum > max_sum:
            max_sum = total_sum
            sub_matrix = [first_row,second_row,third_row]

print(f"Sum = {max_sum}")
for row in sub_matrix:
    print(' '.join(str(el) for el in row))