from utils import Category, Product


def test_category_initialization():
    products = [Product("Product1", "Description1", 10.99, 50), Product("Product2", "Description2", 20.99, 30)]
    category = Category("Category1", "Category Description", products)
    assert category.name == "Category1"
    assert category.description == "Category Description"
    assert category.products == products


def test_product_initialization():
    product = Product("Product1", "Description1", 10.99, 50)
    assert product.name == "Product1"
    assert product.description == "Description1"
    assert product.price == 10.99
    assert product.quantity_in_stock == 50


def test_load_data_from_json():
    assert Category.total_categories == 1


