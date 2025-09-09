import re

sentence = input().strip()

word = input().strip()


pattern = fr'\b{word}\b'


matches = re.findall(pattern, sentence, flags=re.IGNORECASE)

print(len(matches))