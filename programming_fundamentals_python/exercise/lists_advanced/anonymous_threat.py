COMMAND = False

single_string = input().split()

while not COMMAND:
    current_input = input().split()

    if current_input == ['3:1']:
        COMMAND = True

    if current_input[0] == 'merge':
        start_index = int(current_input[1])
        end_index = int(current_input[2])

        if start_index < 0:
            start_index = 0

        if end_index > len(single_string) - 1:
            end_index = len(single_string) - 1

        word = ""
        for i in range(start_index, end_index + 1):
            word += single_string[i]

        del single_string[start_index:end_index + 1]

        single_string.insert(start_index, word)

    elif current_input[0] == 'divide':
        index = int(current_input[1])
        partitions = int(current_input[2])
        word = single_string.pop(index)
        divided_word = []
        if partitions > 0:
            step_size = (len(word) // partitions)
            for _ in range(partitions - 1):
                divided_word.append(word[0:step_size])
                word = word[step_size::]
            if len(word) > 0:
                divided_word.append(word)
        else:
            divided_word.append(word)

        for i in range(len(divided_word)):

            single_string.insert(index + i, divided_word[i])

print(' '.join(single_string))