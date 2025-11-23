from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product : Product):
        self.products.append(product)

    def find(self, product_name):
        product = [p for p in self.products if p.name == product_name][0]
        return product

    def remove(self, product_name):
        try:
            product = [p for p in self.products if p.name == product_name][0]
            self.products.remove(product)
        except IndexError:
            pass
    def __repr__(self):
        output = ""
        for p in self.products:
            output += f"{p.name}: {p.quantity}\n"
        return output[:-1]