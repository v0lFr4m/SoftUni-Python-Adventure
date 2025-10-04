n = int(input())

matrix = []
knights = []

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == "K":
            knights.append([row,col])

removed_knights = 0
possible_movies = [(1 , 2), (2, 1), (-1 , 2), (2 , -1), (1 , -2),(-2, 1), (-1 , -2), (-2 , -1)]
while True:
    max_hits = 0
    max_knight = [0, 0]

    for k_row , k_col in knights:
        hits = 0
        for move in possible_movies:
            current_row = k_row + move[0]
            current_col = k_col + move[1]

            if 0 <= current_row < n and 0 <= current_col < n:
                if matrix[current_row][current_col] == 'K':
                    hits += 1

        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    if max_hits == 0:
        break
    else:
        knights.remove(max_knight)
        matrix[max_knight[0]][max_knight[1]] = '0'
        removed_knights += 1

print(removed_knights)
