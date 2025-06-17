initial_array = list(map(int, input().split()))
command = input()
while command[0] != "end":
    command = input().split()
    if command[0] == 'swap':
        index1 = int(command[1])
        index2 = int(command[2])

        pass
    elif command[0] == 'multiply':
        index1 = int(command[1])
        index2 = int(command[2])
        pass

    elif command[0] == 'decrease':
        initial_array = [(i - 1) for i in initial_array]
        print(initial_array)
