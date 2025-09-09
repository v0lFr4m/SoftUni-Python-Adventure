houses = list(map(int, input().split('@')))
index = 0

while True:
    command = input().split()
    if command[0] == "Love!":
        break
    index += int(command[1])

    if index >= len(houses):
        index = 0

    if houses[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        houses[index] -= 2
        if houses[index] == 0:
            print(f"Place {index} has Valentine's day.")
print(f"Cupid's last position was {index}.")
failed_houses = sum(1 for house in houses if house > 0)
if failed_houses == 0:
    print('Mission was successful.')
else:
    print(f"Cupid has failed {failed_houses} places.")
