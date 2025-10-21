def cookbook(*args):
    cuisine = {}
    # this is compacted version
    for name, cuisine_name, ingredients in args:
        cuisine.setdefault(cuisine_name, []).append((name, ingredients))

    # not compacted version
    # if cuisine not in cuisine_dict:
    #     cuisine_dict[cuisine] = []
    # cuisine_dict[cuisine].append((name, ingredients))

    for cuisine_name in cuisine:
        cuisine[cuisine_name].sort(key=lambda x: x[0])

    sorted_cuisines = sorted(cuisine.items(), key=lambda x: (-len(x[1]), x[0]))

    output = []
    for cuisine_name , recipes_list in sorted_cuisines:
        output.append(f"{cuisine_name} cuisine contains {len(recipes_list)} recipes:")
        for recipe_name, ingredients in recipes_list:
            ingredients_as_string = ', '.join(ingredients)
            output.append(f"  * {recipe_name} -> Ingredients: {ingredients_as_string}")
    return "\n".join(output)




print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
