def command_fire(_index : int , _damage : int):
    if 0 <= _index < len(warship):
        warship[index] -= damage
        if warship[index] <= 0:
           return "You won! The enemy ship has sunken."

def command_defend(_start_index : int , _end_index : int , _damage : int):
    if 0 <= _start_index <= _end_index < len(pirate_ship):
        for i in range(_start_index, _end_index + 1):
            pirate_ship[i] -= _damage
            if pirate_ship[i] <= 0:
                return True
    return False

def command_repair(_index : int , _heath : int , _max_health : int):
    if 0 <= index < len(pirate_ship):
        pirate_ship[index] += health
        if pirate_ship[index] > max_health:
            pirate_ship[index] = max_health

def command_status():
    threshold = max_health * 0.2
    count = sum(1 for section in pirate_ship if section < threshold)
    return f"{count} sections need repair."


pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())

while True:
    command = input()
    if command == "Retire":
        break
    current_command = command.split()
    if current_command[0] == 'Fire':
        index = int(current_command[1])
        damage = int(current_command[2])
        result = command_fire(index , damage)
        if result:
            print(result)
            exit()


    elif current_command[0] == 'Defend':

        start_index = int(current_command[1])
        end_index = int(current_command[2])
        damage = int(current_command[3])
        if command_defend(start_index, end_index , damage):
            print("You lost! The pirate ship has sunken.")
            exit()



    elif current_command[0] == "Repair":
        index = int(current_command[1])
        health = int(current_command[2])
        command_repair(index , health , max_health)

    elif current_command[0] == 'Status':
        result = command_status()
        if result:
            print(result)


print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")

