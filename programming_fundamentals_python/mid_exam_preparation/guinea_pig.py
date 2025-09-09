quantity_of_food = float(input()) * 1000
quantity_of_hay = float(input()) * 1000
quantity_of_cover = float(input()) * 1000
pig_weight_in_kilograms = float(input()) * 1000
days = 0
IS_ENOUGH = True

while days < 30:

    quantity_of_food -= 300
    days += 1

    if quantity_of_food <= 0:
        IS_ENOUGH = False
        break

    if days % 2 == 0:
        hay = int(quantity_of_food * 0.05)
        quantity_of_hay -= hay
        if quantity_of_hay <= 0:
            IS_ENOUGH = False
            break

    if days % 3 == 0:
        needed_cover = pig_weight_in_kilograms // 3
        quantity_of_cover -= needed_cover
        if quantity_of_cover <= 0:
            IS_ENOUGH = False
            break

if IS_ENOUGH and days !=0:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food / 1000:.2f}, Hay: {quantity_of_hay/1000:.2f}, Cover: {quantity_of_cover /1000:.2f}.")
elif not IS_ENOUGH:
    print("Merry must go to the pet store!")
