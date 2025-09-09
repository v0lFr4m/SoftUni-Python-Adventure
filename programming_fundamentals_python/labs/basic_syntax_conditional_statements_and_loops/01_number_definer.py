number = float(input())

if number > 0 :
    if 1 > number > 0:
        print("small positive")
    elif number > 1_000_000 :
        print("large positive")
    else:
        print('positive')
elif number < 0 :
    if 0 > number > -1:
        print("small negative")
    elif number < -1_000_000 :
        print('large negative')
    else:
        print("negative")
else:
    print('zero')