from collections import deque
from datetime import datetime, timedelta
robots = input().split(';')
starting_time = input().split(':')

start_time = datetime.strptime(":".join(starting_time), "%H:%M:%S")

robot_data = {}
products = deque()

for i in range(len(robots)):
    robot_name, process_time = robots[i].split('-')
    robot_data[robot_name] = int(process_time)


while (line := input()) != 'End':
    products.append(line)

robots_busy = {name: start_time for name in robot_data}
current_time = start_time

while products:
    current_time += timedelta(seconds=1)  
    product = products.popleft()
    assigned = False


    for name, process_time in robot_data.items():
        if robots_busy[name] <= current_time:
            robots_busy[name] = current_time + timedelta(seconds=process_time)
            print(f"{name} - {product} [{current_time.strftime('%H:%M:%S')}]")
            assigned = True
            break

    if not assigned:
        products.append(product)