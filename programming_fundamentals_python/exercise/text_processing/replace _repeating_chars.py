string = input()
new_string = ''
last_added_char = ''
for char in string:
    if char != last_added_char:
        new_string += char
        last_added_char = char
print(new_string)


