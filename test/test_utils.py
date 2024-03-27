from utils import Category, Product
import pytest


def test_load_data_from_json():
    assert Category.total_categories == []


def test_create_category():
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации,"
                                     " но и получение дополнительных функций для удобства жизни")
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации,"
                                    " но и получение дополнительных функций для удобства жизни")
    assert category.products == ''


def test_category_product_list():
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации,"
                                     " но и получение дополнительных функций для удобства жизни")
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category.add_product(product)
    expected_output = "Iphone 15, 210000.0 руб. Stock: 8 шт."
    assert category.products == expected_output


def test_price_setter():
    product = Product("Widget", "Gadget", 10.0, 50)
    with pytest.raises(ValueError):
        product.price = -5


@pytest.fixture
def sample_category_data():
    return [
        {"name": "Category 1", "description": "Description 1", "products": []},
        {"name": "Category 2", "description": "Description 2", "products": []}
    ]


def test_add_product_to_category():
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, "
                                     "но и получение дополнительных функций для удобства жизни")
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category.add_product(product)
    assert product in category._Category__products
    assert Category.total_unique_products == 1


def test_products():
    category = Category("Category 1", "Description 1")
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 150.0, 5)
    category.add_product(product1)
    category.add_product(product2)
    expected_output = "Product 1, 100.0 руб. Stock: 10 шт.\nProduct 2, 150.0 руб. Stock: 5 шт."
    assert category.products == expected_output


def test_add_product():
    category = Category("Category 1", "Description 1")
    product = Product("Product 1", "Description 1", 100.0, 10)
    category.add_product(product)
    assert product in category._Category__products
    assert len(Category.unique_product_names) == 3
    assert Category.total_unique_products == 3
