sequence_of_nums = tuple(map(float , input().split()))

data = {}

for el in sequence_of_nums:
    if el not in data:
        data[el] = sequence_of_nums.count(el)

for key, value in data.items():
    print(f"{key:.1f} - {value} times")