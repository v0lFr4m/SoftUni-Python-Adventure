import re

text = input()

pattern = r"(?P<symbol>@|#)(?P<word_one>[A-Za-z]{3,})(?P=symbol){2}(?P<word_two>[A-Za-z]{3,})(?P=symbol)"

matches = list(re.finditer(pattern, text))
mirrored_words = []

for match in matches:
    first_word = match.group('word_one')
    second_word = match.group('word_two')
    if first_word == second_word[::-1]:
        mirrored_words.append(f"{first_word} <=> {second_word}")

if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

if mirrored_words:
    print("The mirror words are:")
    print(', '.join(mirrored_words))
else:
    print('No mirror words!')