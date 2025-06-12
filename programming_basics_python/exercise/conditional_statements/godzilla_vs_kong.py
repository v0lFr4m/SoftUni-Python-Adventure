DECOR = 0.10
DISCOUNT = 0.10

budget = float(input())
number_of_stasists = int(input())
price_clothing = float(input())

decor_price = budget * DECOR

if number_of_stasists > 150:
    total_sum = number_of_stasists * price_clothing
    total_sum = total_sum - (total_sum * DISCOUNT)
    total_sum += decor_price
else:
    total_sum = number_of_stasists * price_clothing + decor_price
if budget >= total_sum :
    result = abs(budget - total_sum)
    print("Action!")
    print(f"Wingard starts filming with {result:.2f} leva left.")
else:
    result = abs(budget - total_sum)
    print ("Not enough money!")
    print(f"Wingard needs {result:.2f} leva more.")