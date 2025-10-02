n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary = [matrix[i][i] for i in range(n)]
secondary = [matrix[i][n - 1 - i] for i in range(n)]

primary_sum = sum(primary)
secondary_sum = sum(secondary)

difference = abs(primary_sum - secondary_sum)
print(difference)