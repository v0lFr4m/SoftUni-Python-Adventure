def replace_with_lower_letters(some_string_ :str):
    return  some_string_.lower()

def replace_with_upper_letters(some_string_: str):
    return some_string_.upper()

def reverse(start_index_: int , end_index_: int , some_string_: str):
    if 0 <= start_index_ <= end_index_ < len(some_string_):
        reversed_string = ''
        for i in range(start_index_ , end_index_ + 1):
            reversed_string += some_string_[i]
        return reversed_string[::-1]

def substring(substring_ : str , some_string_ : str):
    if substring_ in some_string_:
        new_string = some_string_.replace(substring_, "")
        return new_string
    else:
        return f"The username {some_string_} doesn't contain {substring_}."

def replace(some_string_ : str , char : str):
    some_string_ = some_string_.replace(char, "-")
    return some_string_

def is_valid(some_string_ : str , char:str):
    if char in some_string_:
        return f"Valid username."
    else:
        return f"{char} must be contained in your username."


some_string = input()

while (command := input()) != 'Registration':
    current_command = command.split()
    if current_command[0] == 'Letters':
        if current_command[1] == 'Lower':
            some_string = replace_with_lower_letters(some_string)
            print(some_string)

        elif current_command[1] == 'Upper':
            some_string = replace_with_upper_letters(some_string)
            print(some_string)

    elif current_command[0] == 'Reverse':
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        reversed_word = reverse(start_index , end_index , some_string)
        if reversed_word is not None:
            print(reversed_word)

    elif current_command[0] == 'Substring':
        current_substring = current_command[1]
        print(substring(current_substring , some_string))

    elif current_command[0] == 'Replace':
        current_char = current_command[1]
        some_string = replace(some_string , current_char)
        print(some_string)

    elif current_command[0] == 'IsValid':
        current_char = current_command[1]
        print(is_valid(some_string , current_char))

