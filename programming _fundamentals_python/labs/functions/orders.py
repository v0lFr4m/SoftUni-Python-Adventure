def calculating_price(product :str, quanityty: int):
    if product == 'coffee':
        return quanityty * 1.50
    elif product == 'water':
        return  quanityty * 1.00
    elif product == 'coke':
        return  quanityty * 1.40
    elif product == 'snacks':
        return  quanityty * 2.00

current_product = input()
current_quantity = int(input())

print(f"{calculating_price(current_product , current_quantity):.2f}")
