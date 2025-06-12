product = input()

type_of_product = ""

if product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" or product == "grapes":
    type_of_product += "fruit"
elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
    type_of_product += "vegetable"
else:
    type_of_product += "unknown"
print(type_of_product)