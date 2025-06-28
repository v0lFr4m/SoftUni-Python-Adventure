friends_list  = input().split(', ')
lost_names = 0
blacklisted_names = 0
while True:
    command = input()
    if command == "Report":
        break
    current_command = command.split()
    if current_command[0] == 'Blacklist':
        name = current_command[1]
        if name in friends_list:
            index = friends_list.index(name)
            friends_list.remove(name)
            friends_list.insert(index , 'Blacklisted')
            blacklisted_names += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    if current_command[0] == 'Error':
        index = int(current_command[1])
        if 0 <= index < len(friends_list) and friends_list[index] != 'Blacklisted' and friends_list[index] != 'Lost':
            name = friends_list[index]
            friends_list.pop(index)
            friends_list.insert(index , 'Lost')
            lost_names += 1
            print(f"{name} was lost due to an error.")
    if current_command[0] == 'Change':
        index = int(current_command[1])
        new_name = current_command[2]
        if 0 <= index < len(friends_list):
            current_name = friends_list[index]
            friends_list.pop(index)
            friends_list.insert(index , new_name)
            print(f"{current_name} changed his username to {new_name}.")
print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_names}")
print(' '.join(i for i in friends_list))
