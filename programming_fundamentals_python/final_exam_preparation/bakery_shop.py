def receive(quantity_ , food_ , stocks_):
    if quantity_ <= 0:
        return
    if food_ not in stocks_:
        stocks_[food_] = 0
    stocks_[food_] += quantity_

def sell(quantity_, food_, stocks_, sold_quantities_):
    if food_ not in stocks_:
        return f"You do not have any {food_}.", sold_quantities_

    current_quantity = stocks_.get(food_)
    if current_quantity < quantity_:
        sold_quantities_ += current_quantity
        stocks_.pop(food_)
        return f"There aren't enough {food_}. You sold the last {current_quantity} of them.", sold_quantities_
    else:
        stocks_[food_] -= quantity_
        sold_quantities_ += quantity_
        if stocks_[food_] == 0:
            stocks_.pop(food_)
        return f"You sold {quantity_} {food_}.", sold_quantities_

sold_quantities = 0
stocks = {}
while (line := input()) != 'Complete':
    line = line.split()
    quantity = int(line[1])
    food = line[2]

    if line[0] == 'Receive':
        receive(quantity , food, stocks)

    elif line[0] == 'Sell':
        sold_items, sold_quantities = sell(quantity , food , stocks , sold_quantities)
        print(sold_items)
for food , qty in stocks.items():
    print(f"{food}: {qty}")
print(f"All sold: {sold_quantities} goods")