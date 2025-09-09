def next_version(x1 : int , x2 : int , x3: int) :
    current_version[2] += 1
    if current_version[2] > 9:
        current_version[2] = 0
        current_version[1] += 1
        if current_version[1] > 9:
            current_version[1] = 0
            current_version[0] += 1
    return f"{current_version[0]}.{current_version[1]}.{current_version[2]}"
current_version = list(map(int,input().split('.')))

print(next_version(current_version[0] , current_version[1] , current_version[2]))
