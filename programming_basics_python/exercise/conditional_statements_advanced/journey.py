budget = float(input())
season = input()

total = 0
destination = ""
place_to_stay = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        total = budget * 0.30
        place_to_stay = "Camp"
    else:
        total = budget * 0.70
        place_to_stay = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        total = budget * 0.40
        place_to_stay = "Camp"
    else:
        total = budget * 0.80
        place_to_stay = "Hotel"
else:
    destination = "Europe"
    place_to_stay = "Hotel"
    total = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{place_to_stay} - {total:.2f}")


