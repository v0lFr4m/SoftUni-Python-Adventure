materials = {"shards" : 0 , "fragments" : 0, "motes" : 0}
junk = {}
is_obtained = False
REQUIRED_MATERIAL = 250

while not is_obtained:
    line = input().lower().split()

    for i in range(0 , len(line) ,2 ):
        current_material = line[i + 1]
        current_quantity = int(line[i])

        if current_material == "shards":
            materials[current_material] += current_quantity
            if materials[current_material] >= REQUIRED_MATERIAL:
                materials[current_material] -= REQUIRED_MATERIAL
                print("Shadowmourne obtained!")
                is_obtained = True
                break

        elif current_material == "fragments":
            materials[current_material] += current_quantity
            if materials[current_material] >= REQUIRED_MATERIAL:
                materials[current_material] -= REQUIRED_MATERIAL
                print("Valanyr obtained!")
                is_obtained = True
                break

        elif current_material == "motes":
            materials[current_material] += current_quantity
            if materials[current_material] >= REQUIRED_MATERIAL:
                materials[current_material] -= REQUIRED_MATERIAL
                print("Dragonwrath obtained!")
                is_obtained = True
                break
        else:
            if current_material in junk:
                junk[current_material] += current_quantity
            else:
                junk[current_material] = current_quantity

for material in ["shards", "fragments", "motes"]:
    print(f"{material}: {materials[material]}")

for material, quantity in junk.items():
    print(f"{material}: {quantity}")