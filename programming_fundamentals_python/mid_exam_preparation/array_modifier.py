initial_array = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == 'end':
        break
    if command[0] == 'swap':
        index1 = int(command[1])
        index2 = int(command[2])
        initial_array[index1] , initial_array[index2] =  initial_array[index2] , initial_array[index1]


    if command[0] == 'multiply':
        index1 = int(command[1])
        index2 = int(command[2])

        initial_array[index1] *= initial_array[index2]

    if command[0] == 'decrease':
        initial_array = [(i - 1) for i in initial_array]

print(', '.join(str(i) for i in initial_array))
