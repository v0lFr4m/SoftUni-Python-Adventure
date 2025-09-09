names_list = input().split(', ')

sorting_names = sorted(names_list, key=lambda x: (-len(x) , x))

print(sorting_names)
