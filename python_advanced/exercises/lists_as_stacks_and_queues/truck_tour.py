from collections import deque

number_of_pumps = int(input())

truck_tanks = 0

pumps = deque()

for _ in range(number_of_pumps):
    petrol , distance = list(map(int, input().split()))
    pumps.append((petrol , distance))

start = 0
stop = 0

while stop <= start:
    fuel = 0
    for petrol , distance in pumps:
        fuel += petrol
        if fuel <distance:
            pumps.rotate(-1)
            start += 1
            stop = 0
            break
        fuel -= distance
        stop += 1

print(start)