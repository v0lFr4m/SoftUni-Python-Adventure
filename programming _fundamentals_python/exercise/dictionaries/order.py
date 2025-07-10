products = {}

while (line := input()) != "buy":
    name , price , quantity = line.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = [price , quantity]
    else:
        products[name][0] = price  # Update price
        products[name][1] += quantity  # Add quantity

for name, (price, quantity) in products.items():
    total_price = price * quantity
    print(f"{name} -> {total_price:.2f}")
