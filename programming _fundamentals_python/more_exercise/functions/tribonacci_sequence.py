
def tribonacci_sequence(num):
    sequence = [1]

    for i in range(1, num):

        if len(sequence) < 3:
            sequence.append(i)
        else:
            sequence.append(sum(sequence[-3:]))

    return ' '.join([str(num) for num in sequence])

number = int(input())

print(tribonacci_sequence(number))