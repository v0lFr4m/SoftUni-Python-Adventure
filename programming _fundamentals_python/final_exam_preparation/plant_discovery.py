def rate(plants, plant_name, rating):
    if plant_name in plants:
        plants[plant_name]['ratings'].append(rating)
    else:
        print("error")

def update(plants, plant_name, new_rarity):
    if plant_name in plants:
        plants[plant_name]['rarity'] = new_rarity
    else:
        print("error")

def reset(plants, plant_name):
    if plant_name in plants:
        plants[plant_name]['ratings'] = []
    else:
        print("error")



plants_data = {}
number_of_plants = int(input())

for _ in range(number_of_plants):
    plant_name_input, rarity_input = input().split("<->")
    plants_data[plant_name_input] = {
        'rarity': int(rarity_input),
        'ratings': []
    }

while (command := input()) != 'Exhibition':
    if command.startswith("Rate:"):
        _, rest = command.split("Rate: ")
        plant, rating = rest.split(" - ")
        rating = float(rating)
        rate(plants_data, plant.strip(), rating)

    elif command.startswith("Update:"):
        _, rest = command.split("Update: ")
        plant, new_rarity = rest.split(" - ")
        new_rarity = int(new_rarity)
        update(plants_data, plant.strip(), new_rarity)


    elif command.startswith("Reset:"):
        _, plant = command.split("Reset: ")
        reset(plants_data, plant.strip())


print("Plants for the exhibition:")
for plant, data in plants_data.items():
    avg_rating = sum(data['ratings']) / len(data['ratings']) if data['ratings'] else 0
    print(f"- {plant}; Rarity: {data['rarity']}; Rating: {avg_rating:.2f}")