lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
FIGHT_COUNTER = 0
HELMET = 0
SWORD = 0
SHIELD = 0
ARMOR = 0


for fight in range(1 ,lost_fights_count + 1):
    if fight % 2 == 0:
        HELMET += 1
    if fight % 3 == 0:
        SWORD += 1
        if fight % 2 == 0:
            SHIELD += 1
            if SHIELD % 2 == 0:
                ARMOR += 1

total = HELMET * helmet_price + SWORD * sword_price + SHIELD * shield_price + ARMOR * armor_price
print(f"Gladiator expenses: {total:.2f} aureus")