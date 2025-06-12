#PRICE PER MENU
CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DESERT_PRICE_PERCENT = 0.20
DELIVERY_PRICE = 2.50

#INPUT
number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())

#CALCOLATIONS
total_menu = number_chicken_menu * CHICKEN_MENU_PRICE + number_fish_menu * FISH_MENU_PRICE + number_vegetarian_menu * VEGETARIAN_MENU_PRICE
total_menu = total_menu + (total_menu * DESERT_PRICE_PERCENT)
total_order = total_menu + DELIVERY_PRICE
print(f"{total_order:.2f}")