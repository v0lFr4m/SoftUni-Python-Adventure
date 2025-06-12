TANK_CAPACITY = 255
liters = 0
tank_water = 0
number_of_lines = int(input())

for i in range(number_of_lines):
    add_water = int(input())
    if (liters + add_water) > 255:
        print('Insufficient capacity!')
    else:
        liters += add_water
print(liters)

