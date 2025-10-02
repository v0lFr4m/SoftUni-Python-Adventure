rows , cols = list(map(int, input().split(', ')))

matrix = []

for _ in range(rows):
    data = list(map(int, input().split(', ')))
    matrix.append(data)
max_sum = float('-inf')
sub_matrix = []

for row_index in range(rows-1):
    for cols_index in range(cols-1):
        current_element = matrix[row_index][cols_index]
        next_element = matrix[row_index][cols_index + 1]
        element_below = matrix[row_index + 1][cols_index]
        diagonal_element = matrix[row_index + 1][cols_index + 1]
        sum_elements = current_element + next_element + element_below + diagonal_element

        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [
                [current_element , next_element],
                [element_below , diagonal_element]
            ]
print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)