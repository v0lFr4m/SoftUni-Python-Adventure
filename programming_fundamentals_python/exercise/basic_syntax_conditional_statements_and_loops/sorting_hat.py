
while True:
    command = input()
    if command == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    word = len(command)
    if command != "Voldemort":
        if word < 5:
            print(f"{command} goes to Gryffindor.")
        elif word == 5 :
            print(f"{command} goes to Slytherin.")
        elif word == 6:
            print(f"{command} goes to Ravenclaw.")
        elif word > 6:
            print(f"{command} goes to Hufflepuff.")
    else:
        print("You must not speak of that name!")
        break
