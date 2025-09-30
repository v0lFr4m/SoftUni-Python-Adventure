expression = input().split()
result = 0
numbers = []
for token in expression:
    if token.lstrip('-').isdigit():
        numbers.append(int(token))
    else:
        if token == '+':
            result = sum(numbers)
        elif token == '-':
            result = numbers[0]
            for n in numbers[1:]:
                result -= n
        elif token == '*':
            result = 1
            for n in numbers:
                result *= n
        elif token == '/':
            result = numbers[0]
            for n in numbers[1:]:
                result //= n

        numbers = [result]


print(numbers[0])
