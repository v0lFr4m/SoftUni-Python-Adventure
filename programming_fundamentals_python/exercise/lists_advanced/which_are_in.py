def check_substring(substring):
    return any(substring in word for word in strings_list)


substrings_list = input().split(', ')
strings_list = input().split(', ')

final_list = list(filter(lambda sub_word: check_substring(sub_word), substrings_list))

print(final_list)