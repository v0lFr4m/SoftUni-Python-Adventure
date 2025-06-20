dungeon_rooms = input().split('|')

initial_health = 100
initial_bitcoins = 0
best_room = 0
YOU_ARE_ALIVE = True
for current_room in dungeon_rooms:
    best_room += 1
    room = current_room.split()
    if room[0] == 'potion':
        current_amount_healing = int(room[1])
        initial_health += current_amount_healing
        if initial_health >= 100:
            current_health = 100 - (initial_health - current_amount_healing)
            initial_health = 100
            print(f"You healed for {current_health} hp.")
            print(f"Current health: {initial_health} hp.")
        else:
            print(f"You healed for {current_amount_healing} hp.")
            print(f"Current health: {initial_health} hp.")

    if room[0] == 'chest':
        current_amount_bitcoins = int(room[1])
        initial_bitcoins += current_amount_bitcoins
        print(f"You found {current_amount_bitcoins} bitcoins.")

    if room[0] != 'potion' and room[0] != 'chest':
        current_monster = room[0]
        current_damage = int(room[1])
        initial_health -= current_damage
        if initial_health <= 0:
            print(f"You died! Killed by {current_monster}.")
            print(f"Best room: {best_room}")
            YOU_ARE_ALIVE = False
            break
        else:
            print(f"You slayed {current_monster}.")
if YOU_ARE_ALIVE:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")



