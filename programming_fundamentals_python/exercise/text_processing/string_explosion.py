string = input()
final_string = ''
strength = 0
for index in range(len(string)):
    # explosion
    if strength > 0 and string[index] != ">":
        strength -= 1

    # explosion mark
    elif string[index] == '>':
        final_string += '>'
        strength += int(string[index + 1])

    else:
        final_string += string[index]
print(final_string)
