energy = int(input())
wins = 0
command = input()
while command != 'End of battle':
    enemy_distance = int(command)
    if energy < enemy_distance:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        energy -= enemy_distance
        break
    energy -= enemy_distance
    wins += 1
    if wins % 3 == 0:
        energy += wins
    command = input()
if energy >= 0:
    print(f"Won battles: {wins}. Energy left: {energy}")

