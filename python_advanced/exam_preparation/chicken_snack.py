from collections import deque

amount_of_money  = list(map(int, input().split()))
prices_sequence = deque(map(int, input().split()))
food_count = 0
while amount_of_money and prices_sequence:
    current_money = amount_of_money.pop() # LAST ELEMENT
    current_price = prices_sequence.popleft() # FIRST ELEMENT

    if current_money == current_price:
        food_count += 1

    elif current_money > current_price:
        food_count += 1
        diff = current_money - current_price
        if prices_sequence:
            amount_of_money[-1] += diff
        else:
            continue

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
elif food_count < 4 and food_count != 0:
    print(f"Henry ate: {food_count} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")