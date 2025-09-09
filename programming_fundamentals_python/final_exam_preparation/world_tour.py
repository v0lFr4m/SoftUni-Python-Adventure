def add_stop (some_string :str, index : int, string:str) -> str:
    if 0 <= index < len(some_string):
        return some_string[:index] + string + some_string[index:]
    return some_string  # Return original if indices are invalid
def remove_stop(some_string: str, start_index: int, end_index: int) -> str:
    if 0 <= start_index <= end_index < len(some_string):
        return some_string[:start_index] + some_string[end_index + 1:]
    return some_string  # Return original if indices are invalid

def switch_stop(some_of_string :str , old_string : str , new_string : str)-> str:
    return  some_of_string.replace(old_string , new_string)


some_string = input()

while (command := input()) != 'Travel':
    line = command.split(':')
    action = line[0]
    if action == 'Add Stop':
        index = int(line[1])
        string = line[2]
        some_string = add_stop(some_string , index , string)
        print(some_string)
    elif action == "Remove Stop":
        start_index = int(line[1])
        end_index = int(line[2])
        some_string = remove_stop(some_string , start_index , end_index)
        print(some_string)
    elif action == 'Switch':
        old_string = line[1]
        new_string = line[2]
        some_string = switch_stop(some_string , old_string , new_string)
        print(some_string)

print(f"Ready for world tour! Planned stops: {some_string}")