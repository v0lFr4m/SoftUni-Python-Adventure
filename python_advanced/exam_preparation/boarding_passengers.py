def boarding_passengers(available_capacity ,*args):
    boarded = {}

    for passengers , plan in args:
        if available_capacity == 0:
            break

        if passengers <= available_capacity:
            boarded[plan] = boarded.get(plan, 0) + passengers
            available_capacity -= passengers
        else:
            continue

    sorted_boarded = sorted(boarded.items(), key=lambda x: (-x[1],x[0]))
    result = ["Boarding details by benefit plan:"]
    for plan , count in sorted_boarded:
        result.append(f"## {plan}: {count} guests")

    total_boarded = sum(boarded.values())
    total_requested = sum(group[0] for group in args)

    if total_boarded == total_requested:
        result.append("All passengers are successfully boarded!")
    elif available_capacity == 0 and total_boarded < total_requested:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")
    else:
        result.append(f"Partial boarding completed. Available capacity: {available_capacity}.")
    return "\n".join(result)



print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))