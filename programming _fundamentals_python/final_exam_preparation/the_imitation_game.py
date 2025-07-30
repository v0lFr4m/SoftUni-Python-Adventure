def move(num_of_letters :int , message : str):

    """ Moves the first n letters to the back of the string """

    return message[num_of_letters:] + message[:num_of_letters]

def insert(index_: int , value_ : str , message: str):

    """ Inserts the given value before the given index in the string """

    return message[:index_] + value_ + message[index_:]

def change_all(substring_: str , replacement_: str , message_ : str):

    """ Changes all occurrences of the given substring with the replacement text """

    return message_.replace(substring_, replacement_)

encrypted_message = input()

while (command := input()) != 'Decode':
    command = command.split("|")
    if command[0] == "Move":
        numbers_of_letters = int(command[1])
        encrypted_message = move(numbers_of_letters , encrypted_message)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]

        encrypted_message =  insert(index, value, encrypted_message)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = change_all(substring , replacement , encrypted_message)

print(f"The decrypted message is: {encrypted_message}")