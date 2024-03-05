import json


def load_data_from_json(file_path):
    categories = []

    with open(file_path, 'r') as file:
        data = json.load(file)
        for category_data in data:
            products = []
            for product_data in category_data['products']:
                product = Product(product_data['name'], product_data['description'],
                                  product_data['price'], product_data['quantity'])
                products.append(product)
                category = Category(category_data['name'], category_data['description'], products)
                categories.append(category)
    return categories


class Category:
    total_categories = 0
    total_unique_products = set()

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1


class Product:
    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        Category.total_unique_products.add(name)