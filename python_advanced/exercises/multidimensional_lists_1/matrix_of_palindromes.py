rows , cols = list(map(int , input().split()))

start_pos = ord("a")

for row in range(rows):
    for col in range(cols):
        print(f"{chr(start_pos + row)}{chr(start_pos + row + col)}{chr(start_pos + row)}", end=" ")
    print()