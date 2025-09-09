def command_urgent(_item : str , _groceries : list) -> list:
    if _item not in _groceries:
        _groceries.insert(0 , _item)
        return _groceries


def command_unnecessary(_item : str , _groceries : list) -> list:
    if _item in _groceries:
        _groceries.remove(_item)
        return _groceries

def command_correct(_old_item : str , _new_item : str, _groceries : list) -> list:
    if _old_item in _groceries:
        old_item_index = _groceries.index(_old_item)
        _groceries.pop(old_item_index)
        _groceries.insert(old_item_index , _new_item)
        return _groceries

def command_rearrange(_item : str , _groceries : list) -> list:
    if _item in _groceries:
        _groceries.remove(_item)
        _groceries.append(_item)
        return _groceries

groceries = input().split('!')

while True:
    command = input().split()
    if command[0] == 'Go' and command[1] == "Shopping!":
        break

    if command[0] == 'Unnecessary':
        item = command[1]
        command_unnecessary(item , groceries)


    if command[0] == 'Urgent':
        item = command[1]
        command_urgent(item , groceries)

    if command[0] == 'Correct':
        old_item = command[1]
        new_item = command[2]
        command_correct(old_item , new_item , groceries)

    if command[0] == 'Rearrange':
        item = command[1]
        command_rearrange(item , groceries)
print(', '.join(str(i) for i in groceries))

