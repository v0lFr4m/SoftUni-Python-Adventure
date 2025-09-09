from collections import deque

liters = int(input())

queue = deque()



while (name := input()) != 'Start':
    queue.append(name)


while (data := input()) != 'End':
    if data.startswith('refill'):
        liters_to_fill = int(data.split()[-1])
        liters += liters_to_fill
    elif data.isdigit():
        name = queue.popleft()
        liters_wanted = int(data)
        if liters_wanted <= liters:
            liters -= liters_wanted
            print(f'{name} got water')
        else:
            print(f"{name} must wait")

print(f"{liters} liters left")