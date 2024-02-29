import pytest

from utils import Category, Product

def_category_initialization():
    category = Category("Test Category", "This is a test category")
    assert category.name == " Category"
    assert.description == "This is a test category"
    assert category.products == []

def test_product_initialization():
    product = Product("Test Product", "This is a test product", 10.99, 100)
    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 10.99
    assert product.quantity_in_stock == 100

def test_total_categories():
    assert Category.total_categories == 0
    category1 = Category("Category 1", "Description 1")
    assert Category.total_categories == 1

def test_total_unique_products():
    assert len(Category.total_unique_products) == 0
    product1 = Product("Product 1", "Description 1", 9.99, 50)
    assert len(Category.total_unique_products) == 1