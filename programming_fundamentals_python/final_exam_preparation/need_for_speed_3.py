MAX_FUEL_CAPACITY = 75
MIN_MILEAGE = 10_000
MAX_MILEAGE = 100_000

def drive(car_name: str, distance_km: int, fuel_needed: int, cars_data: dict):
    if cars_data[car_name]['fuel'] >= fuel_needed:
        cars_data[car_name]['fuel'] -= fuel_needed
        cars_data[car_name]['mileage'] += distance_km
        result = f"{car_name} driven for {distance_km} kilometers. {fuel_needed} liters of fuel consumed."
        if cars_data[car_name]['mileage'] >= MAX_MILEAGE:
            del cars_data[car_name]
            result += f"\nTime to sell the {car_name}!"
        return result
    else:
        return "Not enough fuel to make that ride"

def refuel(car_name: str, fuel_to_add: int, cars_data: dict):
    current_fuel = cars_data[car_name]['fuel']
    actual_fuel_added = min(fuel_to_add, MAX_FUEL_CAPACITY - current_fuel)
    cars_data[car_name]['fuel'] += actual_fuel_added
    return f"{car_name} refueled with {actual_fuel_added} liters"

def revert(car_name: str, kilometers_to_revert: int, cars_data: dict):
    cars_data[car_name]['mileage'] -= kilometers_to_revert
    if cars_data[car_name]['mileage'] < MIN_MILEAGE:
        cars_data[car_name]['mileage'] = MIN_MILEAGE
        return None
    else:
        return f"{car_name} mileage decreased by {kilometers_to_revert} kilometers"

num_cars = int(input())
cars = {}

for _ in range(num_cars):
    car_name_input, mileage_input, fuel_input = input().split('|')
    cars[car_name_input] = {
        "mileage": int(mileage_input),
        "fuel": int(fuel_input)
    }

while (user_command := input()) != 'Stop':

    command_parts = user_command.split(" : ")
    command_type = command_parts[0]
    car_model = command_parts[1]

    if command_type == "Drive":
        drive_distance = int(command_parts[2])
        fuel_required = int(command_parts[3])
        print(drive(car_model, drive_distance, fuel_required, cars))

    elif command_type == "Refuel":
        fuel_amount = int(command_parts[2])
        print(refuel(car_model, fuel_amount, cars))

    elif command_type == "Revert":
        kilometers = int(command_parts[2])
        revert_result = revert(car_model, kilometers, cars)
        if revert_result:
            print(revert_result)

for car_model, car_info in cars.items():
    print(f"{car_model} -> Mileage: {car_info['mileage']} kms, Fuel in the tank: {car_info['fuel']} lt.")



