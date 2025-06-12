PREMIERE = 12
NORMAL = 7.50
DISCOUNT = 5


cinema_show = input()
rolls = int(input())
columns = int(input())
hall = rolls * columns
total = 0

if cinema_show == "Premiere":
    total += hall * PREMIERE
elif cinema_show == "Normal":
    total += hall * NORMAL
elif cinema_show == "Discount":
    total += hall * DISCOUNT
print(f"{total:.2f}")