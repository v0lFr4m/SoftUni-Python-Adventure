import re
number = []

string = input()

pattern = r'\d+'

while string != '':
    number += re.findall(pattern, string)

    string = input()

print(' '.join(number))