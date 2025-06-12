import sys

numbers = int(input())
MAX_NUM = -sys.maxsize
MIN_NUM = sys.maxsize
for i in range(numbers):
    current_number = int(input())
    if current_number > MAX_NUM:
        MAX_NUM = current_number
    if current_number < MIN_NUM:
        MIN_NUM = current_number
print(f"Max number: {MAX_NUM}")
print(f"Min number: {MIN_NUM}")
