import math

number = int(input())
prime = True

if number > 1:
    for i in range(2, math.floor(math.sqrt(number) + 1)):
        if number % i == 0:
            prime = False
            break
else:
    prime = False

if prime:
    print('True')
else:
    print('False')