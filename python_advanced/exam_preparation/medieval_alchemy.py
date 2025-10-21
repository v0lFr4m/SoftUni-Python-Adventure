from collections import deque
required_potion = {"Brew of Immortality" : 110,
                   "Essence of Resilience" : 100,
                   "Draught of Wisdom" : 90,
                    "Potion of Agility" : 80,
                   "Elixir of Strength" : 70}


elixir_of_strength = 70
crafted_potions = []
substances = list(map(int, input().split(', ')))
crystal_energy = deque(map(int, input().split(', ')))

while not len(crafted_potions) == 5 and substances and crystal_energy:
    substance = substances.pop()
    energy = crystal_energy.popleft()
    combined_energy = substance + energy

    for name , needed_energy in required_potion.items():
        if combined_energy == needed_energy and name not in crafted_potions:
                crafted_potions.append(name)
                break
    else:
        max_name = ''
        max_energy = 0
        for name , needed_energy in required_potion.items():
            if name not in crafted_potions and combined_energy > needed_energy > max_energy:
                max_name = name
                max_energy = needed_energy
                break
        if max_name != '' and max_name not in crafted_potions:
            crafted_potions.append(max_name)
            energy -= 20
            if energy > 0:
                crystal_energy.append(energy)
        else:
            energy -= 5
            if energy > 0:
                crystal_energy.append(energy)


if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")
if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")
if substances:
    print(f"Substances: {', '.join(str(i) for i in reversed(substances))}")
if crystal_energy:
    print(f"Crystals: {', '.join(str(i) for i in crystal_energy)}")
