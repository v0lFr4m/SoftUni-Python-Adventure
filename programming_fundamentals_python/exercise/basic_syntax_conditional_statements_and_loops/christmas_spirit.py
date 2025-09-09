
ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLAND = 3
TREE_LIGHTS = 15
TOTAL = 0
EARNED_SPIRIT = 0
quantity_of_decorations = int(input())
remaining_days = int(input())

for day in range (1 , remaining_days + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        TOTAL += ORNAMENT_SET * quantity_of_decorations
        EARNED_SPIRIT += 5
    if day % 3 == 0 :
        TOTAL += (TREE_SKIRT + TREE_GARLAND) * quantity_of_decorations
        EARNED_SPIRIT += 10 + 3
    if day % 5 == 0 :
        TOTAL += TREE_LIGHTS * quantity_of_decorations
        EARNED_SPIRIT += 17
        if day % 3 == 0:
            EARNED_SPIRIT += 30
    if day % 10 == 0 :
        EARNED_SPIRIT -= 20
        TOTAL += TREE_SKIRT + TREE_GARLAND + TREE_LIGHTS
if remaining_days % 10 == 0:
    EARNED_SPIRIT -= 30
print(f"Total cost: {TOTAL}")
print(f"Total spirit: {EARNED_SPIRIT}")
