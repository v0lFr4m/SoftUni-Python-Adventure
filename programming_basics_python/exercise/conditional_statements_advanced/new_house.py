ROSE = 5
DAHLIA = 3.80
TULIP = 2.80
NARCISSUS = 3
GLADIOLUS = 2.50

flower = input()
quantity = int(input())
budget = int(input())

total = 0
if flower == "Roses":
    if quantity > 80:
        total = quantity * ROSE
        total = total - (total * 0.10) #DISCOUNT 10%
    else:
        total = quantity * ROSE
elif flower == "Dahlias":
    if quantity > 90:
        total = quantity * DAHLIA
        total = total - (total * 0.15)  # DISCOUNT 15%
    else:
        total = quantity * DAHLIA
elif flower == "Tulips":
    if quantity > 80:
        total = quantity * TULIP
        total = total - (total * 0.15)  # DISCOUNT 15%
    else:
        total = quantity * TULIP
elif flower == "Narcissus":
    if quantity < 120:
        total = quantity * NARCISSUS
        total = total + (total * 0.15)  # MORE EXPENSIVE  15%
    else:
        total = quantity * NARCISSUS
elif flower == "Gladiolus":
    if quantity < 80:
        total = quantity * GLADIOLUS
        total = total + (total * 0.20)  # MORE EXPENSIVE  20%
    else:
        total = quantity * GLADIOLUS
if budget >= total:
    total = abs(total - budget)
    print(f"Hey, you have a great garden with {quantity} {flower} and {total:.2f} leva left.")
else:
    total = abs(total - budget)
    print(f"Not enough money, you need {total:.2f} leva more.")