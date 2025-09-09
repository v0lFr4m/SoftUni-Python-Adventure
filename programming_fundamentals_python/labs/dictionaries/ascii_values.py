list_of_chars = input().split(', ')


my_dict = {list_of_char: ord(list_of_char) for list_of_char in list_of_chars}
print(my_dict)