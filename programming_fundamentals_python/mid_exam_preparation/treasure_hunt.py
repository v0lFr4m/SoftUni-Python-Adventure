initial_treasure_chest = input().split('|')

while True:
    command = input()
    if command == "Yohoho!":
        break

    current_command = command.split()

    if current_command[0] == 'Loot':
        for treasure in current_command[1:]:
            if treasure not in initial_treasure_chest:
                initial_treasure_chest.insert(0, treasure)

    if current_command[0] == 'Drop':
        index = int(current_command[1])
        if 0 <= index < len(initial_treasure_chest):
            item = initial_treasure_chest.pop(index)
            initial_treasure_chest.append(item)

    if current_command[0] == 'Steal':
        count = int(current_command[1])
        stolen_items = initial_treasure_chest[-count:] if count < len(initial_treasure_chest) else initial_treasure_chest[:]
        initial_treasure_chest = initial_treasure_chest[:-count] if count < len(initial_treasure_chest) else []
        print(", ".join(stolen_items))


if not initial_treasure_chest:
    print("Failed treasure hunt.")
else:
    total_length = sum(len(item) for item in initial_treasure_chest)
    average = total_length / len(initial_treasure_chest)
    print(f"Average treasure gain: {average:.2f} pirate credits.")