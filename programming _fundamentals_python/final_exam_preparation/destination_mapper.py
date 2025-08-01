import re

text = input()

pattern = r"(=|/)([A-Z][a-zA-Z]{2,})\1"

matches = re.findall(pattern, text)

destinations = [match[1] for match in matches]
travel_points = sum(len(dest) for dest in destinations)


# travel_points = 0
# destinations = []
# for match in matches:
#     destinations.append(match[1])
#
# for dest in destinations:
#     travel_points += len(dest)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")