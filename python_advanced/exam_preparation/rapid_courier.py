from collections import deque

packages = list(map(int, input().split()))
couriers = deque(map(int, input().split()))

total_weight = 0

while packages and couriers:
    package = packages.pop()      # last package
    capacity = couriers.popleft() # first courier capacity
    if package == capacity:
        total_weight += package

    elif capacity >= package:
        capacity -= package * 2
        if capacity > 0:
            couriers.append(capacity)
        total_weight += package
    elif package > capacity:
        remaining_weight = package - capacity
        total_weight += capacity
        packages.append(remaining_weight)

print(f'Total weight: {total_weight} kg')

if not packages and not couriers:
    print('Congratulations, all packages were delivered successfully by the couriers today.')
elif packages:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join([str(i) for i in packages])}")
elif couriers:
    print(f"Couriers are still on duty: {', '.join([str(i) for i in couriers])} but there are no more packages to deliver.")
