PACK_OF_PENCILS_PRICE = 5.80
PACK_OF_MARKERS_PRICE = 7.20
AGENT_PER_LITER_PRICE = 1.20

number_of_pencils = int(input())
number_of_markers = int(input())
liters_of_agent = int(input())
discount_percent = int(input())

total_sum = (number_of_pencils * PACK_OF_PENCILS_PRICE + number_of_markers * PACK_OF_MARKERS_PRICE + liters_of_agent * AGENT_PER_LITER_PRICE)
total_sum = total_sum - (total_sum * discount_percent/100)
print(f"{total_sum:.2f}")

