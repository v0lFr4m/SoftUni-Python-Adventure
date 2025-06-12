PUZZLE = 2.60
DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2
DISCOUNT = 0.35
RENT = 0.10

vac_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total = number_of_puzzles * PUZZLE + number_of_dolls * DOLL + number_of_teddy_bears * TEDDY_BEAR + number_of_minions * MINION + number_of_trucks * TRUCK
total_toys = number_of_trucks + number_of_minions + number_of_dolls + number_of_puzzles + number_of_teddy_bears
if total_toys >= 50:
    total = total - (total * DISCOUNT)
total = total - (total * RENT)
if vac_price > total :
    total = abs(total - vac_price)
    print(f"Not enough money! {total:.2f} lv needed.")
else:
    total = abs(total - vac_price)
    print(f"Yes! {total:.2f} lv left.")





