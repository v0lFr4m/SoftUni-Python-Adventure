text = input()

unique_symbols = set()

for char in text:
    unique_symbols.add(char)
for char in sorted(unique_symbols):
    print(f"{char}: {text.count(char)} time/s")