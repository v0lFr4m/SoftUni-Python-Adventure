def even_odd(*args):
    command = args[-1]
    even = []
    odd = []
    for num in range(len(args) -1):
        if args[num] % 2 == 0:
            even.append(args[num])
        else:
            odd.append(args[num])
    if command == 'even':
        return even
    elif command == 'odd':
        return odd

