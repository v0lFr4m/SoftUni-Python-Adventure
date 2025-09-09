import re


number_of_input = int(input())
pattern = r"(\|)(?P<boss_name>[A-Z]{4,})(\|):#(?P<words>[A-Za-z]+ [A-Za-z]+)#$"
string = ''
for _ in range(number_of_input):
    text = input()
    string += text
    if re.match(pattern, text):
        match = re.match(pattern, text)
        boss_name = match.group('boss_name')
        title = match.group('words')
        print(f"{boss_name}, The {title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")
