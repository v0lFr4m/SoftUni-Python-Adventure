#PRICE

SNEAKERS_PERCENT_FROM_TASK_OF_YEAR = 0.40
SWEAT_SUIT_PERCENT_FROM_SNEAKERS = 0.20
BASKETBALL_PRICE_FROM_SWEAT_SUIT = 4
ACCESSORIES_PRICE_FROM_BASKETBALL = 5

#INPUT
year_tax = int(input())


#CALCOLATIONS

sneakers_price = year_tax - (year_tax * SNEAKERS_PERCENT_FROM_TASK_OF_YEAR)
sweat_suit_price = sneakers_price - (sneakers_price * SWEAT_SUIT_PERCENT_FROM_SNEAKERS)
basketball_price = sweat_suit_price / BASKETBALL_PRICE_FROM_SWEAT_SUIT
accessories_price = basketball_price / ACCESSORIES_PRICE_FROM_BASKETBALL
total_sum = sneakers_price + sweat_suit_price + basketball_price + accessories_price + year_tax
print(f"{total_sum:.2f}")