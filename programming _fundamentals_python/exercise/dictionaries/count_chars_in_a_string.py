words = input().split()
char_count = {}

for word in words:
    for char in word:
        char_count[char] = char_count.get(char, 0) + 1

for i in char_count:
    print(f"{i} -> {char_count[i]}")