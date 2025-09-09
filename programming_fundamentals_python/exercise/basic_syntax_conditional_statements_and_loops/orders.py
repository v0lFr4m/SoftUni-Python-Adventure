orders = int(input())
total = 0

for order in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    price_for_coffe = price_per_capsule * days * capsules_per_day
    if 1 <= days <= 31 and 1 <= capsules_per_day <= 2000 and 0.01 <= price_per_capsule <= 100.00:
        total += price_for_coffe
        print(f"The price for the coffee is: ${price_for_coffe:.2f}")
print(f"Total: ${total:.2f}")

