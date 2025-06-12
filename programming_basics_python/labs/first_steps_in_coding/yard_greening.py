PRICE_PER_SQR_METER = 7.61
DISCOUNT = 0.18

sqr_meters = float(input())
sum_sqr_meters = sqr_meters * PRICE_PER_SQR_METER
discount = sum_sqr_meters * 0.18
final_price = sum_sqr_meters - discount
print(f"The final price is :{final_price} lv.")
print(f"The discount is {discount} lv.")
