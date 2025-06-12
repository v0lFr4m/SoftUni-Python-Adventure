
def multiply(a , b):
    return a * b

def divide(a , b):
    return int(a / b)

def subtract(a , b):
    return a - b

def add(a , b):
    return a + b

def calculator(operator, a , b):
    result = 0
    if operator == "multiply":
        result = multiply(a , b)
    elif operator == 'divide':
        result = divide(a , b )
    elif operator == 'add':
        result = add(a , b )
    elif operator == 'subtract':
        result = subtract(a , b )
    print(result)

input_operator = input()
first_num = int(input())
second_num = int(input())

calculator(input_operator , first_num , second_num)