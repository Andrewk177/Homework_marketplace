import json
from abc import ABC, abstractmethod


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


class ObjectCreationLogger:
    def __repr__(self):
        attributes = ', '.join(f"{key}={value!r}" for key, value in self.__dict__.items())
        return f"{self.__class__.__name__}({attributes})"


class PurchasableItem(ABC, ObjectCreationLogger):
    @abstractmethod
    def total_cost(self):
        pass


class Item(ABC):
    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self._price = price
        self.quantity_in_stock = quantity_in_stock
        print(self)

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(Item, PurchasableItem):
    def __init__(self, name, description, price, quantity_in_stock):
        super().__init__(name, description, price, quantity_in_stock)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Введена некорректная цена.")
        else:
            self._price = value

    @classmethod
    def create_product_from_dict(cls, product_data):
        return cls(**product_data)

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return Product(
            name=f"{self.name} & {other.name}",
            description=f"{self.description} | {other.description}",
            price=self.price + other.price,
            quantity_in_stock=self.quantity_in_stock + other.quantity_in_stock
        )

    def total_cost(self):
        return self._price * self.quantity_in_stock


class Order(PurchasableItem):
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = self.total_cost()
        print(self)

    def total_cost(self):
        return self.product.price * self.quantity


class Smartphone(Product):
    def __init__(self, name, description, price, quantity_in_stock, performance, model, memory, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if not isinstance(other, Smartphone):
            raise TypeError("Cannot add objects of different types.")


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity_in_stock, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if not isinstance(other, LawnGrass):
            raise TypeError("Cannot add objects of different types.")


class ZeroQuantityError(Exception):
    def __init__(self, message="Товар с нулевым количеством не может быть добавлен."):
        self.message = message
        super().__init__(self.message)


try:
    quantity = 0
    if quantity == 0:
        raise ZeroQuantityError
    print("Товар добавлен.")
except ZeroQuantityError as e:
    print(e)
finally:
    print("Обработка добавления товара завершена.")


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
        if isinstance(product, Product):
            if product.quantity_in_stock == 0:
                raise ValueError("Добавление товара с нулевым количеством.")
            self.__products.append(product)
            Category.unique_product_names.add(product.name)
            Category.total_unique_products = len(Category.unique_product_names)
            print("Товар добавлен.")
        else:
            raise TypeError("Можно добавлять только продукты.")
        print("Обработка добавления товара завершена.")

    def average_price(self):
        try:
            if len(self.__products) == 0:
                raise ZeroDivisionError
            return sum(product.price for product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0
        finally:
            print("Обработка завершена.")
