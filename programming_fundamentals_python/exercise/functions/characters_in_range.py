def char_in_range(first , second):
    string_of_chars = []
    for char in range(ord(first) + 1 , ord(second)):
        string_of_chars.append(chr(char))
    return string_of_chars
first_char = input()
second_char = input()
all_chars = char_in_range(first_char , second_char)
print(" ".join(all_chars))
