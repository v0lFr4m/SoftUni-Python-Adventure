list_of_vowels = ['a', 'o', 'u', 'e', 'i','A', 'U', 'E', 'I', 'O']

text = input()
removed_vowels = ''.join([x for x in text if x not in list_of_vowels])

print(removed_vowels)