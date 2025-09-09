import re

sentence = input()

pattern = r'(?<!_)_([A-Za-z0-9]+)(?![A-Za-z0-9_])'
match = re.findall(pattern , sentence)

print(','.join(match))