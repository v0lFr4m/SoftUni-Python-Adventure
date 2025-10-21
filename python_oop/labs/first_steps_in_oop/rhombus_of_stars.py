def print_row(spaces , stars):
    print(f"{' ' * spaces}{'* ' * stars}")

def top(n):
    for row in range(1, n+1):
        print_row(n-row, row)

def bottom(n):
    for row in range(1 , n):
        print_row(row , n-row)

def print_rombus(n):
    top(n)
    bottom(n)

n = int(input())

print_rombus(n)
