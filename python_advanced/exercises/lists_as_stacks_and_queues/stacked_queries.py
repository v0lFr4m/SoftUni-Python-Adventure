num = int(input())
stacked_queries = []
for i in range(num):
    current_command = input().split()
    number = int(current_command[0])

    if number == 1:
        queries = int(current_command[1])
        stacked_queries.append(queries)

    elif number == 2 and stacked_queries:
        stacked_queries.pop()

    elif number == 3 and stacked_queries:
        print(max(stacked_queries))

    elif number == 4 and stacked_queries:
        print(min(stacked_queries))


print(", ".join(map(str, reversed(stacked_queries))))