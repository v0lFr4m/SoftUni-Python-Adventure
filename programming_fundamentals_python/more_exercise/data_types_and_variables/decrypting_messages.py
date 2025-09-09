key = int(input())
number_of_lines = int(input())
decrypted = ''

for i in range(number_of_lines):
    crypt = input()
    decrypt = chr(ord(crypt) + key)
    decrypted += decrypt
print(decrypted)