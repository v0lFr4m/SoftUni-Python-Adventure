first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'Add':
        if command[1] == 'First':
            for num in command:
                if num.isdigit():
                    first_sequence.add(int(num))

        elif command[1] == 'Second':
            for num in command:
                if num.isdigit():
                    second_sequence.add(int(num))

    elif command[0] == 'Remove':
        if command[1] == 'First':
            for num in command:
                if num.isdigit() and int(num) in first_sequence:
                    first_sequence.remove(int(num))

        elif command[1] == 'Second':
            for num in command:
                if num.isdigit() and int(num) in second_sequence:
                    second_sequence.remove(int(num))
    elif command[0] == 'Check' and command[1] == 'Subset':
        is_subset = second_sequence.issubset(first_sequence)
        if is_subset:
            print('True')
        else:
            print('False')

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')