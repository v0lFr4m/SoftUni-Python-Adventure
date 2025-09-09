def change_string(string : str , char : str , replacement_char : str):
    result = string.replace(char, replacement_char)
    return result

def includes_string(string : str , substring : str):
    if substring in string:
        return True
    else:
        return False

def end_substring(string : str , substring : str ):
    if string.endswith(substring):
        return True
    else:
        return False

def uppercase(string : str):
    return string.upper()

def find_index(string :str , char: str):
    return string.index(char)

def cut_string(string: str, start_index : int , count: int):
    result = string[start_index:start_index + count]
    return result
some_string = input()

while (command := input()) != 'Done':
    line = command.split()
    action = line[0]

    if action == "Change":
        char = line[1]
        char_replacement = line[2]
        some_string = change_string(some_string , char , char_replacement)
        print(some_string)

    elif action == 'Includes':
        substring = line[1]
        result = includes_string(some_string, substring)
        if result:
            print('True')
        else:
            print('False')

    elif action == 'End':
        substring = line[1]
        result = end_substring(some_string , substring)
        if result:
            print('True')
        else:
            print('False')

    elif action == "Uppercase":
        some_string = uppercase(some_string)
        print(some_string)

    elif action == 'FindIndex':
        char = line[1]
        result = find_index(some_string , char)
        print(result)

    elif action == 'Cut':
        start_index = int(line[1])
        count = int(line[2])
        result = cut_string(some_string , start_index , count)
        print(result)

