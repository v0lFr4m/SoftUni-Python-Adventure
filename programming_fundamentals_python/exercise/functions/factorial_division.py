import math


def factorial_division(first : int , second : int) -> float:
    first_factorial = math.factorial(first)
    second_factorial = math.factorial(second)
    return first_factorial / second_factorial



first_number = int(input())
second_number = int(input())

print(f"{factorial_division(first_number, second_number):.2f}")
