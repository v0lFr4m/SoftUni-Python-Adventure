def grocery_store(**products):
    sorted_products = sorted(
        products.items(),
        key=lambda x: (-x[1], -len(x[0]), x[0])
    )

    result = [f"{name}: {quantity}" for name, quantity in sorted_products]

    return '\n'.join(result)
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
