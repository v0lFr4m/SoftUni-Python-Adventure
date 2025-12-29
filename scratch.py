car_list = {}
inserted_cars = {}
while (line := input("INSERT DATA : ")) != 'end':
    command = line.split()
    car_number = int(command[0])
    car_model = str(command[1])
    passport_validation = bool(command[2])

    if car_number in car_list.keys():
        car_list[car_number] += [car_model , passport_validation]
    else:
        car_list[car_number] = [car_model , passport_validation]

while (line := input("Insert car number , model , passport status : ")) != car_list:
    command = line.split()
    car_number = int(command[0])
    car_model = str(command[1])
    passport_validation = bool(command[2])

    for key in car_list.keys():
        if key == car_number:
            for model , passport in car_list.values():
                if model == car_model and passport == passport_validation:
                    car_list.pop(key)
                    if passport:
                        inserted_cars[key] = [model , passport]
                        print("Car is inside parking lot")
                    else:
                        car_list.pop(key)
                        print("Car doesn't has passport")



# 1236545 toyota True
# 1111111 bmw False
# 2222222 audi False
# 3333333 porche True
