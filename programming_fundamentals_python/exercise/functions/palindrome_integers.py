def is_palindrome(some_number_as_string: str) -> bool:
    return some_number_as_string == some_number_as_string[::-1]
number_as_string = input().split(", ")
for current_number_as_string in number_as_string:
    print(is_palindrome(current_number_as_string))