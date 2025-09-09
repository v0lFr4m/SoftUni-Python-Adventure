energy = 100

starting_coins = 100

events = input().split('|')

events = [event.split('-') for event in events]

success = True

for event in events:

    if event[0] == 'rest':
        add_energy = int(event[1])
        if energy + add_energy > 100:
            energyAdded = 100 - energy  # point 1
            energy = 100  # point 1
            print(f"You gained {energyAdded} energy.")  # point 1
            print(f"Current energy: {energy}.")

        else:
            print(f"You gained {add_energy} energy.")
            energy += add_energy
            print(f"Current energy: {energy}.")

    elif event[0] == 'order':
        energy_loss = 30

        if energy - energy_loss >= 0:  # point 2
            print(f"You earned {int(event[1])} coins.")
            starting_coins += int(event[1])
            energy -= energy_loss

        else:
            print(f"You had to rest!")
            energy += 50

    elif starting_coins - int(event[1]) >= 0:  # point 3
        print(f'You bought {event[0]}.')

        starting_coins -= int(event[1])
    else:
        print(f"Closed! Cannot afford {event[0]}.")
        success = False
        break

if success:
    print("Day completed!")
    print(f"Coins: {starting_coins}")
    print(f"Energy: {energy}")