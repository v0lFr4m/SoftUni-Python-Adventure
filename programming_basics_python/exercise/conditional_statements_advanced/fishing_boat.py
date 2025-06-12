group_budget = int(input())
season = input()
fishermen = int(input())

additional_discount = 1.00
trip_price = 0.00

if season == 'Summer' or season == 'Autumn':
    trip_price = 4200
elif season == 'Spring':
    trip_price = 3000
elif season == 'Winter':
    trip_price = 2600
if fishermen <= 6:
    trip_price *= 0.9
elif fishermen <= 11:
    trip_price *= 0.85
else:
    trip_price *= 0.75
if season != 'Autumn' and fishermen % 2 == 0:
    trip_price *= 0.95

if group_budget >= trip_price:
    print(f'Yes! You have {group_budget - trip_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {trip_price - group_budget:.2f} leva.')