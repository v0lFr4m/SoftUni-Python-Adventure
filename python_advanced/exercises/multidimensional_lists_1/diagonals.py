n = int(input())

matrix = []

for _ in range(n):
    data = list(map(int, input().split(', ')))
    matrix.append(data)
prime_diagonal = []
prime_diagonal_sum = 0
secondary_diagonal = []
secondary_diagonal_sum = 0

for row_index in range(n):
    value = matrix[row_index][row_index]
    prime_diagonal.append(value)
    prime_diagonal_sum += value

for row_index in range(n):
    value = matrix[row_index][n-1 - row_index]
    secondary_diagonal.append(value)
    secondary_diagonal_sum += value

print(f"Primary diagonal: {', '.join(map(str, prime_diagonal))}. Sum: {prime_diagonal_sum}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {secondary_diagonal_sum}")

# solution with comprehension

n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

primary = [matrix[i][i] for i in range(n)]
secondary = [matrix[i][n - 1 - i] for i in range(n)]

print(f"Primary diagonal: {', '.join(map(str, primary))}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary))}. Sum: {sum(secondary)}")