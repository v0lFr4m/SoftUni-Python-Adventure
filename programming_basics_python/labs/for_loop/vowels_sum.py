word = input()
COUNT = 0
for char in word:
    if char == "a":
        COUNT += 1
    elif char == "e":
        COUNT += 2
    elif char == "i":
        COUNT += 3
    elif char == "o":
        COUNT += 4
    elif char == "u":
        COUNT += 5
print(COUNT)