def add(username : str , sent:int , received : int ,list_of_users ):
    if username not in list_of_users:
        list_of_users[username] = {'sent' : sent, 'received' : received}
    return list_of_users

def message(sender , receiver , list_of_users , capacity):
    capacity_reached = []
    if sender in list_of_users and receiver in list_of_users:
        list_of_users[sender]['sent'] += 1
        list_of_users[receiver]['received'] += 1

        if list_of_users[sender]['sent'] + list_of_users[sender]['received'] >= capacity:
            capacity_reached.append(sender)
            del list_of_users[sender]

        if list_of_users[receiver]['sent'] + list_of_users[receiver]['received'] >= capacity:
            capacity_reached.append(receiver)
            del list_of_users[receiver]
    return capacity_reached

def empty(username , list_of_users):
    if username == 'All':
        list_of_users.clear()
    elif username in list_of_users:
        del list_of_users[username]

    return list_of_users


capacity = int(input())
user_list = {}

while (command := input()) != 'Statistics':
    line = command.split('=')
    action = line[0]

    if action == "Add":
        username = line[1]
        sent = int(line[2])
        received = int(line[3])
        user_list = add(username , sent , received , user_list)

    elif action == "Message":
        sender = line[1]
        receiver = line[2]
        reached = message(sender, receiver, user_list, capacity)
        for user in reached:
            print(f"{user} reached the capacity!")

    elif action == 'Empty':
        username = line[1]
        user_list = empty(username , user_list)

print(f"Users count: {len(user_list)}")
for user , data in user_list.items():
    result = data['sent'] + data['received']
    print(f"{user} - {result}")


