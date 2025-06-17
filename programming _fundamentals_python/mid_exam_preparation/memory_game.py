sequence_of_elements = input().split()
moves = 0

while True:
    command = input().split()
    if "end" in command:
        break
    moves += 1
    index_1 = int(command[0])
    index_2 = int(command[1])

    if index_1 == index_2 or index_1 < 0 or index_2 < 0 or\
       index_1 >= len(sequence_of_elements) or\
       index_2 >= len(sequence_of_elements):
        middle = len(sequence_of_elements) // 2
        element_to_add = f"-{moves}a"
        sequence_of_elements.insert(middle, element_to_add)
        sequence_of_elements.insert(middle, element_to_add)
        print("Invalid input! Adding additional elements to the board")
        continue

    if sequence_of_elements[index_1] == sequence_of_elements[index_2]:
        current_element = sequence_of_elements[index_1]
        first_element , second_element = sorted([index_1 ,index_2] , reverse=True)
        sequence_of_elements.pop(first_element)
        sequence_of_elements.pop(second_element)
        print(f"Congrats! You have found matching elements - {current_element}!")
    else:
        print('Try again!')


    if not sequence_of_elements:
        print(f"You have won in {moves} turns!")
        exit()

print('Sorry you lose :(')
print(' '.join(sequence_of_elements))