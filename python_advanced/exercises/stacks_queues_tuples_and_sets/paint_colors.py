from collections import deque

def find_colors(input_string):
    substrings = deque(input_string.split())
    found_colors = []

    main_colors = {"red", "yellow", "blue"}
    secondary_colors = {
        "orange": {"red", "yellow"},
        "purple": {"red", "blue"},
        "green": {"yellow", "blue"}
    }
    temp_colors = []

    while substrings:
        if len(substrings) > 1:
            first = substrings.popleft()
            last = substrings.pop()
            combinations = [first+last, last+first]
        else:
            first = substrings.pop()
            last = ''
            combinations = [first]

        color_found = None
        for combo in combinations:
            if combo in main_colors or combo in secondary_colors:
                color_found = combo
                break

        if color_found:
            temp_colors.append(color_found)
        else:

            new_first = first[:-1] if first else ''
            new_last = last[:-1] if last else ''

            mid = len(substrings)//2
            if new_first:
                substrings.insert(mid, new_first)
            if new_last:
                substrings.insert(mid, new_last)

    main_found = {c for c in temp_colors if c in main_colors}
    for c in temp_colors:
        if c in main_colors:
            found_colors.append(c)
        elif c in secondary_colors and secondary_colors[c].issubset(main_found):
            found_colors.append(c)

    return found_colors

print(find_colors(input()))
