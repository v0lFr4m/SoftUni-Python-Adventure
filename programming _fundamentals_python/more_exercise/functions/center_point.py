import math
def find_closest_point(x1 :int, y1 :int, x2 :int, y2 :int):
    first_distance = math.sqrt((x1 ** 2) + (y1 ** 2))
    second_distance = math.sqrt((x2 ** 2) + (y2 ** 2))
    if first_distance != second_distance:
        if first_distance < second_distance:
            return f"({x1}, {y1})"
        else:
            return f"({x2}, {y2})"
    else:
        return f"({x1}, {y1})"

x_1 = math.floor(float(input()))
y_1 = math.floor(float(input()))
x_2 = math.floor(float(input()))
y_2 = math.floor(float(input()))

print(f"{find_closest_point(x_1 , y_1 , x_2 , y_2)}")
