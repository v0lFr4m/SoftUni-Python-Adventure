word = ""

while True:
    command = input()

    if command == "End":
        break
    if command != "SoftUni":
        for char in command:
            word += (char * 2)
        print(word)
        if word != "":
            word = ""



