
string = input().split()
current_palindrome = input()

palindromes_list = []
check_for_palindrome_in_string = [palindromes_list.append(word) for word in string if word == ''.join(reversed(word))]

print(f'{palindromes_list}')
print(f"Found palindrome {palindromes_list.count(current_palindrome)} times")