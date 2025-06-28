chat = []

while True:
    command = input()
    if command == 'end':
        break
    current_command = command.split()
    if current_command[0] == 'Chat':
        message = current_command[1]
        chat.append(message)

    elif current_command[0] == 'Delete':
        message = current_command[1]
        if message in chat:
            chat.remove(message)

    elif current_command[0] == 'Edit':
        message = current_command[1]
        edited_message = current_command[2]
        if message in chat:
            index = chat.index(message)
            chat.remove(message)
            chat.insert(index , edited_message)

    elif current_command[0] == 'Pin':
        message = current_command[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)

    elif current_command[0] == 'Spam':
        messages = [message for message in current_command if current_command != 'Spam']
        spam = 'Spam'
        if spam in messages:
            messages.remove(spam)
        chat += messages
print('\n'.join(i for i in chat))
