
list_as_string = input().split()
count_of_numbers_to_remove = int(input())

list_as_integers = [int(string) for string in list_as_string]
final_list = []
for num in range(count_of_numbers_to_remove):
    str(list_as_integers.remove(min(list_as_integers)))

result = ', '.join(map(str, list_as_integers))
print(result)

