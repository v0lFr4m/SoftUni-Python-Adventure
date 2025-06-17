
IS_SPECIAL = False
IS_REGULAR = True
price_without_tax = 0
while True:
    current_price = input()
    if current_price == "special" :
        IS_SPECIAL = True
        break
    if current_price == "regular":
        IS_REGULAR = True
        break
    else:
        current_price = float(current_price)
        if current_price > 0:
            price_without_tax += current_price
        else:
            print(f"Invalid price!")
tax = price_without_tax * 0.20
final_price = price_without_tax + tax
if price_without_tax != 0:
    if IS_SPECIAL:
        total = final_price - (final_price * 0.10)
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_without_tax:.2f}$")
        print(f"Taxes: {tax:.2f}$")
        print(f"-----------")
        print(f"Total price: {total:.2f}$")
    else:
        total = final_price
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_without_tax:.2f}$")
        print(f"Taxes: {tax:.2f}$")
        print(f"-----------")
        print(f"Total price: {total:.2f}$")
else:
    print(f"Invalid order!")