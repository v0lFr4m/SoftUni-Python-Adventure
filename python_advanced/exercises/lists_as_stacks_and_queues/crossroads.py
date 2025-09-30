from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
total_cars_passed = 0

while True:
    line = input()

    if line == 'END':
        print("Everyone is safe.")
        print(f"{total_cars_passed} total cars passed the crossroads.")
        break

    if line == 'green':
        current_green = green_light

        while cars and current_green > 0:
            car = cars.popleft()
            car_length = len(car)

            if car_length <= current_green:
                current_green -= car_length
                total_cars_passed += 1
            else:

                remaining = car_length - current_green
                if remaining <= free_window:

                    total_cars_passed += 1
                    current_green = 0
                else:
                    hit_index = current_green + free_window
                    print("A crash happened!")
                    print(f"{car} was hit at {car[hit_index]}.")
                    exit()
                current_green = 0
    else:
        cars.append(line)
