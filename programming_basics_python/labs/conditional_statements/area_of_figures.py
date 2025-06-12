import math

figure = input("figure> ")

if figure == "square":
    a = float(input("a= "))
    area = a * a
    print(area)
elif figure == "rectangle":
    a = float(input("a= "))
    b = float(input("b= "))
    area = a * b
    print(area)
elif figure == "circle":
    r = float(input("r= "))
    area = math.pi * r * r
    print(area)
elif figure == "triangle":
    a = float(input("a= "))
    ha = float(input("ha= "))
    area = (a * ha) / 2
    print(area)