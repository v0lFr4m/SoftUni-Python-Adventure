prices = input().split("|")
budget = float(input())
profit = []
clean_profit = 0

max_prices = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50
}

for price in prices:
    args = price.split("->")
    item_type = args[0]
    item_price = float(args[1])

    if item_type in max_prices:
        if item_price <= max_prices[item_type] and budget >= item_price:
            budget -= item_price
            new_price = item_price + (item_price * 0.40)
            profit.append(new_price)
            clean_profit += new_price - item_price

total = budget + sum(profit)
print(" ".join(f"{x:.2f}" for x in profit))
print(f"Profit: {clean_profit:.2f}")

if total >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")