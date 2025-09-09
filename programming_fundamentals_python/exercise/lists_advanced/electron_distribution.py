distributed_electrons = []
shell = 0
electrons = int(input())
while electrons > 1:
    shell += 1
    numbers_of_shells = 2 * (shell ** 2)
    if electrons < numbers_of_shells:
        numbers_of_shells = electrons
        electrons = 0
    else:
        electrons -= numbers_of_shells
    distributed_electrons.append(numbers_of_shells)
print(distributed_electrons)