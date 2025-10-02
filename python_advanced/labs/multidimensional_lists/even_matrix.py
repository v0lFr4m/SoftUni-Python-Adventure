rows = int(input())

even_matrix = []

for _ in range(rows):
    data = [int(element) for element in input().split(', ') if int(element) % 2 == 0]
    even_matrix.append(data)

print(even_matrix)

# nested comprehension

even_matrix = [[int(element) for element in input().split(', ') if int(element) % 2 == 0] for _ in range(rows)]

print(even_matrix)

# on one line

print([[int(element) for element in input().split(', ') if int(element) % 2 == 0] for _ in range(int(input()))])