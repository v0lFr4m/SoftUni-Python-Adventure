rows = int(input())

nums = []

for i in range(rows):
    data = map(int, input().split(', '))
    nums.extend(data)

print(nums)

# Flattening


# creating matrix
matrix = []
for _ in range(rows):
    data = list(map(int, input().split(', ')))
    matrix.append(data)

# entering in matrix and flattening
flattened = []
for row in matrix:
    for element in row:
        flattened.append(element)

print(matrix)
print(flattened)

# with flattening comprehension

flattened = [element for row in matrix for element in row]

print(flattened)

