text = input()
digits = ''
letters = ''
other = ''
for char in text:
    if char.isdigit():
        digits += char
    elif char.isalnum():
        letters += char
    else:
        other += char
print(digits)
print(letters)
print(other)