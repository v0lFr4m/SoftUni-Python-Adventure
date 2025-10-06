def fill_the_box(*args):
    height, length, width = args[0], args[1], args[2]
    box_capacity = height * length * width
    cubes_left = 0
    for item in args[3:]:
        if item == 'Finish':
            break
        if box_capacity >= item:
            box_capacity -= item
        else:
            cubes_left += item - box_capacity
            box_capacity = 0

    if box_capacity > 0:
        return f"There is free space in the box. You could put {box_capacity} more cubes."
    else:
        return f"No more free space! You have {cubes_left} more cubes."





print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))