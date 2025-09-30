clothes_in_box = list(map(int , input().split()))
capacity = int(input())

total_racks = 1
current_rack = 0
while clothes_in_box:
    if current_rack + clothes_in_box[-1] <= capacity:
        current_rack += clothes_in_box.pop()
    else:
        total_racks += 1
        current_rack = 0

print(total_racks)
