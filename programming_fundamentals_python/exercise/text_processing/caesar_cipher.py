string = input()
encrypted_version = ''

for char in string:
    encrypted_version += chr(ord(char) + 3)

print(encrypted_version)