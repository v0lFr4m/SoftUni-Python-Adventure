import re

input_line = input()

pattern = re.findall(r'([^0-9]+)(\d+)', input_line)

rage_message = ""
for text, count in pattern:
    count = int(count)
    rage_message += text.upper() * count

unique_symbols = set(rage_message)

print(f"Unique symbols used: {len(unique_symbols)}")
print(rage_message)
