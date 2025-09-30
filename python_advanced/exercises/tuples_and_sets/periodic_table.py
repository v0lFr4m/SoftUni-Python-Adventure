# unique_elements = set()
#
# for _ in range(int(input())):
#     for element in input().split():
#         unique_elements.add(element)
#
# print(*unique_elements,sep='\n')'

print(*{element for _ in range(int(input())) for element in input().split()}, sep='\n')