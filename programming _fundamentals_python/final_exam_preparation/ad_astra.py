import re

some_text = input()

pattern = r"([#|])(?P<item>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>10000|\d{1,4})\1"
matches = re.finditer(pattern, some_text)

total_calories = 0
items = []

for match in matches:
    item = match.group("item")
    date = match.group("date")
    calories = int(match.group("calories"))
    total_calories += calories
    items.append((item, date, calories))

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")
for item, date, nutrition in items:
    print(f"Item: {item}, Best before: {date}, Nutrition: {nutrition}")
