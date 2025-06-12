n = int(input())
LEFT_SUM = 0
RIGHT_SUM = 0

for number in range(0, n*2):
    current_num = int(input())
    if number < n:
        LEFT_SUM += current_num
    elif number >= n:
        RIGHT_SUM += current_num

if LEFT_SUM == RIGHT_SUM:
    print('Yes, sum = ' + str(RIGHT_SUM))
else:
    diff = abs(LEFT_SUM - RIGHT_SUM)
    print('No, diff = ' + str(diff))