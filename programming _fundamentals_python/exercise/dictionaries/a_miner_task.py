resources = {}

while (line := input()) != "stop":

    current_resource = line
    quantity = int(input())
    if current_resource not in resources:
        resources[current_resource] = quantity
    else:
        resources[current_resource] = resources.get(current_resource , quantity) + quantity

for i in resources:
    print(f"{i} -> {resources[i]}")