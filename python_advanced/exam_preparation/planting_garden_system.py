def plant_garden(available_space, *args, **kwargs):

    allowed = {name: size for name, size in args}

    planted = {}


    for plant, requested_quantity in sorted(kwargs.items()):
        if plant not in allowed:
            continue


        size_per_one = allowed[plant]

        max_possible = int(available_space // size_per_one)

        to_plant = min(requested_quantity, max_possible)
        if to_plant > 0:
            planted[plant] = to_plant
            available_space -= to_plant * size_per_one

    valid_requests = [p for p in kwargs if p in allowed]

    success = all(planted.get(p, 0) == kwargs[p] for p in valid_requests)


    if success:
        result = f"All plants were planted! Available garden space: {available_space:.1f} sq meters."
    else:
        result = "Not enough space to plant all requested plants!"

    result += "\nPlanted plants:"

    for p, qty in sorted(planted.items()):
        result += f"\n{p}: {qty}"

    return result
