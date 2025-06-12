import math
def find_longer_line(x1 :int, y1 :int, x2 :int, y2 :int, x3 :int, y3 :int, x4 :int, y4 :int):
    x1y1 = math.sqrt((x1 - 0) ** 2 + (y1 - 0) ** 2)
    x2y2 = math.sqrt((x2 - 0) ** 2 + (y2 - 0) ** 2)
    x3y3 = math.sqrt((x3 - 0) ** 2 + (y3 - 0) ** 2)
    x4y4 = math.sqrt((x4 - 0) ** 2 + (y4 - 0) ** 2)

    first_line = x1y1 + x2y2
    second_line = x3y3 + x4y4

    if first_line >= second_line:
        if x1y1 <= x2y2:
            return f"({x1}, {y1})({x2}, {y2})"
        else:
            return f"({x2}, {y2})({x1}, {y1})"
    else:
        if x3y3 <= x4y4:
            return f'({x3}, {y3})({x4}, {y4})'
        else:
            return f'({x4}, {y4})({x3}, {y3})'

x_1 = math.floor(float(input()))
y_1 = math.floor(float(input()))
x_2 = math.floor(float(input()))
y_2 = math.floor(float(input()))
x_3 = math.floor(float(input()))
y_3 = math.floor(float(input()))
x_4 = math.floor(float(input()))
y_4 = math.floor(float(input()))

print(f"{find_longer_line(x_1 , y_1 , x_2 , y_2 , x_3 , y_3 , x_4 , y_4)}")
