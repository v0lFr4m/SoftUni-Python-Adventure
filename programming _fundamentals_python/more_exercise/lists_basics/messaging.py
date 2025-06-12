sequence_of_numbers = input().split()
text = input()
message = []

for num in sequence_of_numbers:
    digit_sum = sum(int(digit) for digit in num)
    index = digit_sum % len(text)
    message.append(text[index])
    text = text[:index] + text[index + 1:]

print(''.join(message))