from itertools import count

COUNTER = 0
while True:
    command = input()
    if command == "END":
        break
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        COUNTER += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        COUNTER += 2
if COUNTER > 5:
    print("You need extra sleep")
else:
    print(COUNTER)
