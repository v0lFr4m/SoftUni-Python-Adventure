def even_odd_filter(**kwargs):
    filtered = {}
    for command, value in kwargs.items():
        if command == 'even':
            filtered[command] = [x for x in value if x % 2 == 0]
        elif command == 'odd':
            filtered[command] = [x for x in value if x % 2 == 1]

    filtered = dict(sorted(filtered.items(), key=lambda x: len(x[1]), reverse=True))
    return filtered


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))