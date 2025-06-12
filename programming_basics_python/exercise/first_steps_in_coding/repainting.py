#PRICES

PROTECTIVE_NYLON_PRICE_PER_SQRM = 1.50
PAINT_PRICE_PER_LITER = 14.50
THINNER_PRICE_PER_LITER = 5.00
BAG_PRICE = 0.40
EXTRA_PAINT_PERCENT = 0.10
EXTRA_PROTECTIVE_NYLON = 2
FOR_ONE_HOUR_PRICE = 0.30

#CALCOLATIONS
nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_for_job = int(input())

nylon = (nylon_needed + EXTRA_PROTECTIVE_NYLON) * PROTECTIVE_NYLON_PRICE_PER_SQRM
paint = ((paint_needed * EXTRA_PAINT_PERCENT) + paint_needed) * PAINT_PRICE_PER_LITER
thinner = thinner_needed * THINNER_PRICE_PER_LITER
total = nylon + paint + thinner + BAG_PRICE
total = (total *FOR_ONE_HOUR_PRICE) * hours_for_job + total

print(f"{total:.2f}")