from collections import deque

materials = list(map(int , input().split()))
magic_level = deque(map(int, input().split()))

total_magic_level = 0

present = {
    'Doll': 150,
    'Wooden train' : 250,
    'Teddy bear' : 300,
    'Bicycle' : 400
}

crafted_presents = {}

while materials and magic_level:
    material = materials[-1]
    magic = magic_level[0]

    if material == 0 and magic == 0:
        materials.pop()
        magic_level.popleft()
        continue
        
    if material == 0:
        materials.pop()
        continue

    if magic == 0:
        magic_level.popleft()
        continue

    total_magic = material * magic

    if total_magic in present.values():
        for name,value in present.items():
            if total_magic == value:
                crafted_presents[name] = crafted_presents.get(name , 0) + 1
                break
        materials.pop()
        magic_level.popleft()

    elif total_magic < 0:
        sum_value = material + magic
        materials.pop()
        magic_level.popleft()
        materials.append(sum_value)

    else:
        magic_level.popleft()
        materials[-1] += 15


success = (crafted_presents.get('Doll', 0) >= 1 and crafted_presents.get('Wooden train', 0) >= 1) or \
          (crafted_presents.get('Teddy bear', 0) >= 1 and crafted_presents.get('Bicycle', 0) >= 1)


if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for name in sorted(crafted_presents):
    print(f"{name}: {crafted_presents[name]}")