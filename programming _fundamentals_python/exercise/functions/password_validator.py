def is_valid(password : str) -> list:
    list_with_error_messages = []
    if 6 > len(password) or len(password) > 10:
        list_with_error_messages.append("Password must be between 6 and 10 characters")

    if not password.isalnum():
        list_with_error_messages.append('Password must consist only of letters and digits')

    digit_counter = 0
    for current_char in password:
        if current_char.isdigit():
            digit_counter += 1

    if digit_counter < 2:
        list_with_error_messages.append("Password must have at least 2 digits")

    return list_with_error_messages

current_password = input()

error_message = is_valid(current_password)

if not error_message:
    print('Password is valid')
else:
    print("\n".join(error_message))
