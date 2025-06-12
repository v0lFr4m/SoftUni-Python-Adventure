
numbers_as_strings = list(map(int,input().split(', ')))

found_index_or_no = map(lambda x: x if numbers_as_strings[x] % 2 == 0 else 'no' ,range(len(numbers_as_strings)))
even_indexes = list(filter(lambda a: a != 'no' , found_index_or_no))
print(even_indexes)