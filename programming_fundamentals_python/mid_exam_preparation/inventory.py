
items = input().split(", ")

while True:
    command = input()
    if command == 'Craft!':
        break
    command = command.split()
    if command[0] == 'Collect':
        item = command[2]
        if not item in items:
            items.append(item)
        else:
            continue
    if command[0] == 'Drop':
        item = command[2]
        if item in items:
            items.remove(item)
        else:
            continue
    if command[0] == 'Combine' and command[1] == 'Items':
        combine_items = command[3].split(':')
        old_item = combine_items[0]
        if old_item in items:
            new_item = combine_items[1]
            old_item_index = [i for i in range(len(items)) if old_item == items[i]]
            items.insert(old_item_index[0] +1, new_item)

    if command[0] == 'Renew':
        item = command[2]
        if item in items:
            items.remove(item)
            items.append(item)
        else:
            continue
print(', '.join(i for i in items))