list_of_gifts = input().split()
command_list = []
while True:
    command = input().split()
    if command[0] == 'No' and command[1] == 'Money':
        break

    if command[0] == "OutOfStock":
        list_of_gifts = [gift if gift != command[1] else 'None' for gift in list_of_gifts]

    elif command[0] == "Required":
        number = int(command[2])
        if 0 <= number < len(list_of_gifts):
            list_of_gifts[number] = command[1]

    elif command[0] == 'JustInCase':
        list_of_gifts[-1] = command[1]

list_of_gifts = [gift for gift in list_of_gifts if gift != 'None']


print(" ".join(list_of_gifts))




