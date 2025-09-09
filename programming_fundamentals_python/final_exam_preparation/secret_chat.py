def insert_space(index : int , message : str ) -> str:
    return message[:index] + ' ' + message[index:]

def reverse_substring(substring: str, message: str,):
    if substring in message:
        start_index = message.find(substring)
        end_index = start_index + len(substring)

        message = message[:start_index] + message[end_index:]

        reversed_sub = substring[::-1]
        message += reversed_sub

        return message
    else:
        return False

def change_all(substring , replacement , message):
    return message.replace(substring, replacement)

concealed_message = input()

while (command := input()) != "Reveal":
    line = command.split(':|:')
    action = line[0]
    if action == 'InsertSpace':
        index = int(line[1])
        concealed_message = insert_space(index , concealed_message)
        print(concealed_message)


    elif action == 'Reverse':
        substring = line[1]
        reversed_word = reverse_substring(substring , concealed_message)
        if reversed_word:
            concealed_message = reverse_substring(substring , concealed_message)
            print(concealed_message)
        else:
            print('error')


    elif action == "ChangeAll":
        substring = line[1]
        replacement = line[2]
        concealed_message = change_all(substring , replacement , concealed_message)
        print(concealed_message)


print(f"You have a new text message: {concealed_message}")