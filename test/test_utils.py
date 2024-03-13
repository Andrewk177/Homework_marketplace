from utils import Category, Product
import pytest


def test_load_data_from_json():
    assert Category.total_categories == 0


def test_create_category():
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации,"
                                     " но и получение дополнительных функций для удобства жизни")
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации,"
                                    " но и получение дополнительных функций для удобства жизни")
    assert category._products == []


def test_add_product_to_category():
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации,"
                                     " но и получение дополнительных функций для удобства жизни")
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category.add_product(product)
    assert product in category._products
    assert Category.total_unique_products == 1


def test_category_product_list():
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации,"
                                     " но и получение дополнительных функций для удобства жизни")
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category.add_product(product)
    expected_output = "Iphone 15, 210000.0 руб. Stock: 8 шт."
    assert category.products == expected_output


def test_create_product():
    existing_product = Product("Samsung S24", "Smartphone", 100000.0, 22)
    product_list = [existing_product]
    new_product = Product.create_product("Samsung S24 ultra", "new Smartphone", 125000.0, 16, product_list)
    assert new_product.quantity_in_stock == 16
    assert new_product.price == 125000.0

    existing_product = Product("Samsung S24", "Smartphone", 100000.0, 22)
    product_list = [existing_product]
    new_product = Product.create_product("Samsung S24 ultra", "new Smartphone", 125000.0, 16, product_list)
    assert new_product.name == "Samsung S24 ultra"
    assert new_product.description == "new Smartphone"
    assert new_product.price == 125000.0
    assert new_product.quantity_in_stock == 16


def test_price_setter():
    product = Product("Widget", "Gadget", 10.0, 50)
    with pytest.raises(ValueError):
        product.price = -5
