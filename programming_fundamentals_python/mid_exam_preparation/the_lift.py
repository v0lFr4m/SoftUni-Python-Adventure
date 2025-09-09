people = int(input())
lift = list(map(int , input().split(' ')))

for wagon in range(len(lift)):
        can_load = min(4 - lift[wagon] , people)
        people -= can_load
        lift[wagon] += can_load

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif len([current_wagon for current_wagon in lift if current_wagon < 4]) > 0:
    print("The lift has empty spots!")

print(f"{' '.join(str(i) for i in lift)}")

