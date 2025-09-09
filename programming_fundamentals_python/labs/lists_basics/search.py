
n = int(input())
word = input()
strings = []

for _ in range(n):
    current_string = input()
    strings.append(current_string)
print(strings)
filtered_strings = []
for current_string in strings:
    if word in current_string:
        filtered_strings.append(current_string)
print(filtered_strings)