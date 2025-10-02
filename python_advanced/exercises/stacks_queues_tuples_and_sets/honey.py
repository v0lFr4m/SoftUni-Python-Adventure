from collections import deque

working_bees = deque(map(int , input().split()))
nectar = list(map(int , input().split()))
symbols = deque(input().split())

honey = 0

operators = {
    '+' : lambda a, b: a + b,
    '-' : lambda a, b: a - b,
    '*' : lambda a, b: a * b,
    '/' : lambda a, b: a / b if b != 0 else 0
}

while working_bees and nectar:
    if nectar[-1] >= working_bees[0]:
        honey += abs(operators[symbols[0]](working_bees[0], nectar[-1]))
        working_bees.popleft()
        nectar.pop()
        symbols.popleft()
    else:
        nectar.pop()


print(f"Total honey made: {honey}")
if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")
elif nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")