def command_shoot(current_index :int , current_power : int) -> list:
    if 0 <= current_index < len(targets):               # CHECKS IF INDEX IS VALID AND IN RANGE
        targets[current_index] -= current_power
        if targets[current_index] <= 0:
            targets.pop(current_index)
    return targets

def command_add(current_index :int , current_value : int) -> list:
    if 0 <= current_index < len(targets):                   # CHECKS IF INDEX IS VALID AND IN RANGE
        targets.insert(current_index, current_value)
    else:
        print("Invalid placement!")
    return targets

def command_strike(current_index :int , current_radius : int ) -> list:
    left_index = current_index - current_radius
    right_index = current_index + current_radius
    if left_index >= 0 and right_index < len(targets):   # CHECKS IF LEFT INDEX AND RIGHT INDEX IS VALID AND IN RANGE
        del targets[left_index:right_index + 1]
    else:
        print("Strike missed!" )
    return targets

IS_END = True
targets = list(map(int , input().split()))

while IS_END:
    command = input().split()

    if command[0] == 'End':
        IS_END = False

    if command[0] == 'Shoot':
        index = int(command[1])
        power = int(command[2])
        command_shoot(index , power)
    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        command_add(index , value)
    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        command_strike(index , radius)

print('|'.join(str(i) for i in targets))