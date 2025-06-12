secret_message = input().split()
reversed_words = []

for current_word in secret_message:
    reversed_word = ''
    current_digit = ''
    word = []
    for char in current_word:
        if char.isdigit():
            current_digit += char
        else:
            word.append(char)
    reverse = word[0], word[-1] = word[-1], word[0]
    for l in word:
        reversed_word += l
    else:
        first_letter = chr(int(current_digit))
        first_letter += reversed_word
        reversed_words.append(first_letter)
print(' '.join(reversed_words))


