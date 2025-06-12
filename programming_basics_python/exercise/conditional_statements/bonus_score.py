BONUS = 0
number = int(input())

if number <= 100:
    BONUS = 5
elif 100 < number <= 1000:
    BONUS = number * 0.20
else:
    BONUS = number * 0.10

if number % 2 == 0:
    BONUS = BONUS + 1
elif number % 10 == 5:
    BONUS = BONUS + 2

print(BONUS)
print(BONUS + number)