wagons = int(input())
train = [wagon * 0 for wagon in range(wagons)]
COMMAND = False
while not COMMAND:
    current_command = input().split()
    if current_command[0] == 'End':
        COMMAND = True

    if current_command[0] == "add":
        index = int(current_command[1])
        train[-1] += index
    elif current_command[0] == 'insert':
        index = int(current_command[1])
        people = int(current_command[2])
        train[index] += people
    elif current_command[0] == 'leave':
        index = int(current_command[1])
        people = int(current_command[2])
        train[index] -= people

print(train)