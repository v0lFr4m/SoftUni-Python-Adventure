number_of_names = int(input())
names = []
for _ in range(number_of_names):
    name = input()
    names.append(name)

for name in set(names):
    print(name)
