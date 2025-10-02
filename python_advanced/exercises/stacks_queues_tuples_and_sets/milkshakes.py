from collections import deque

chocolates = list((map(int ,input().split(', '))))
cups_of_milk = deque(map(int ,input().split(', ')))

milkshakes = 0
while milkshakes < 5 and chocolates and cups_of_milk:

    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue

    if chocolates[-1] <= 0:
        chocolates.pop()
        continue

    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    if chocolates[-1] == cups_of_milk[0]:
        milkshakes += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print("Milk: empty")