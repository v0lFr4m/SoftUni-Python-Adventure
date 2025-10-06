def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

def func_executor(*args):
    result = []
    for func, func_args in args:
        func_result = func(*func_args)
        result.append(f"{func.__name__} - {func_result}")
    return '\n'.join(result)

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
