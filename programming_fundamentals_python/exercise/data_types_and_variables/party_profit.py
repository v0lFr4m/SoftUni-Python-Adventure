import math

group_size = int(input())
days = int(input())
COINS = 0
companions = 0
for day in range(1 , days + 1):
    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    COINS += 50 - (group_size * 2)

    if day % 3 == 0 :
        COINS -= 3 * group_size

    if day % 5 == 0:
        COINS += 20 * group_size

        if day % 3 == 0:
            COINS -= 2 * group_size


print(f"{group_size} companions received {COINS // group_size} coins each.")
