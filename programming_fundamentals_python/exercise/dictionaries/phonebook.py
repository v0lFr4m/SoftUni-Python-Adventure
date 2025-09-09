phone_book = {}
number = 0
while True:
    contact = input().split("-")
    if len(contact) >= 2:
        phone_book[contact[0]] = contact[1]
    else:
        number = int(contact[0])
        break
for i in range(number):
    name = input()
    if name in phone_book:
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")