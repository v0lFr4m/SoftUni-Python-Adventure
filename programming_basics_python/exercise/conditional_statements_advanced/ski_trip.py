ROOM_FOR_ONE_PERSON = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35


days = int(input())
type_of_room = input()
grade = input()

overnight_stay = days - 1
overnight_price = 0.00

if type_of_room == "room for one person":
    overnight_price = overnight_stay * ROOM_FOR_ONE_PERSON

elif type_of_room == "apartment":
    overnight_price = overnight_stay * APARTMENT

    if days <= 10:
        overnight_price = overnight_price - (overnight_price * 0.30) # 30% DISCOUNT for 10 <= days.

    elif days <= 15:
        overnight_price = overnight_price - (overnight_price * 0.35)  # 35% DISCOUNT for between 10 and 15 days.

    else:
        overnight_price = overnight_price - (overnight_price * 0.50)  # 50% DISCOUNT for 15 and more days.

elif type_of_room == "president apartment":
    overnight_price = overnight_stay * PRESIDENT_APARTMENT

    if days <= 10:
        overnight_price = overnight_price - (overnight_price * 0.10) # 10% DISCOUNT for 10 <= days.

    elif days <= 15:
        overnight_price = overnight_price - (overnight_price * 0.15)  # 15% DISCOUNT for between 10 and 15 days.

    else:
        overnight_price = overnight_price - (overnight_price * 0.20)  # 20% DISCOUNT for 15 and more days.

if grade == "positive":
    overnight_price = overnight_price + (overnight_price * 0.25)

elif grade == "negative":
    overnight_price = overnight_price - (overnight_price * 0.10)

print(f"{overnight_price:.2f}")