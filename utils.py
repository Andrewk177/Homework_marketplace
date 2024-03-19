import json


def load_data_from_json(file_path):
    categories = []

    with open(file_path, 'r') as file:
        data = json.load(file)
        for category_data in data:
            category = Category(category_data.get('name'), category_data.get('description'))
            for product_data in category_data.get('products', []):
                product = Product.create_product_from_dict(Product, product_data,
                                                           getattr(category, '_Category__products'))
                category.add_product(product)
            categories.append(category)
        return categories


class Category:
    total_categories = 0
    total_unique_products = 0
    unique_product_names = set()

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

    @property
    def products(self):
        return "\n".join([f"{product.name}, {product.price} руб. Stock: {product.quantity_in_stock} шт."
                          for product in self.__products])

    def add_product(self, product):
        self.__products.append(product)
        Category.unique_product_names.add(product.name)
        Category.total_unique_products = len(Category.unique_product_names)


class Product:
    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self._price = price
        self.quantity_in_stock = quantity_in_stock

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Введена некорректная цена.")
        elif value < self._price:
            confirmation = input("Цена изменилась. Подтвердить? (да/нет): ")
            if confirmation.lower() == 'да':
                self._price = value
        else:
            self._price = value

    @classmethod
    def create_product_from_dict(cls, data, product_list):
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        quantity_in_stock = data.get('quantity')

        for existing_product in product_list:
            if existing_product.name == name:
                existing_product.quantity_in_stock += quantity_in_stock
                existing_product.price = max(existing_product.price, price)
                return existing_product
        else:
            return cls(name, description, price, quantity_in_stock)
