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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity_in_stock} шт."

    def __add__(self, other):
        total_price = (self.price * self.quantity_in_stock) + (other.price * other.quantity_in_stock)
        total_quantity = self.quantity_in_stock + other.quantity_in_stock
        return total_price / total_quantity


class Category:
    total_categories = []
    total_unique_products = 0
    unique_product_names = set()

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.total_categories.append(self)
        Category.total_unique_products += len(set(product.name for product in self.__products))

    @property
    def products(self):
        return "\n".join([f"{product.name}, {product.price} руб. Stock: {product.quantity_in_stock} шт."
                          for product in self.__products])

    def add_product(self, product):
        self.__products.append(product)
        Category.unique_product_names.add(product.name)
        Category.total_unique_products = len(Category.unique_product_names)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def __len__(self):
        return sum(product.quantity_in_stock for product in self.__products)
