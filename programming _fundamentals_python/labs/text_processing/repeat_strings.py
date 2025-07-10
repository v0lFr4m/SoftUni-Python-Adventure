sequence_of_strings = input().split()
new_sequence = ''
for word in sequence_of_strings:
    length = len(word)
    new_sequence += word * length
print(new_sequence)