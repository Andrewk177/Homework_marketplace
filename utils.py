import json


def load_data_from_json(file_path):
    categories = []

    with open(file_path, 'r') as file:
        data = json.load(file)
        for category_data in data:
            category = Category(category_data['name'], category_data['description'])
            for product_data in category_data['products']:
                product = Product(product_data['name'], product_data['description'],
                                  product_data['price'], product_data['quantity'])
                category.products.append(product)
                categories.append(category)
    return categories


class Category:
    total_categories = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        unique_products = set()
        for product in products:
            unique_products.add(product.name)
        Category.total_unique_products = len(unique_products)


class Product:
    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
