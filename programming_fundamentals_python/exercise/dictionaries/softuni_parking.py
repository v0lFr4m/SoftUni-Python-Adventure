parking_lot = {}

number_of_commands = int(input())
for i in range(number_of_commands):
    command = input().split()


    if command[0] == "register":
        username = command[1]
        license_plate_number = command[2]
        if username not in parking_lot:
            parking_lot[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif command[0] == 'unregister':
        username = command[1]
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            parking_lot.pop(username)
            print(f"{username} unregistered successfully")

for name in parking_lot:
    print(f"{name} => {parking_lot[name]}")