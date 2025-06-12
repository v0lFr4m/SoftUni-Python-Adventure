notes = [0] * 10


while True:
    current_input = input().split('-')
    if current_input[0] == 'End':
        break
    index = int(current_input[0])
    note = current_input[1]
    notes.pop(index - 1)
    notes.insert(index - 1 , note)

result = [element for element in notes if element != 0]
print(result)
