from unittest.mock import patch

import pytest

from src.Category_class import Category
from src.Product_class import Product


# Фикстуры для создания тестовых данных
# Фикстура для создания категории
@pytest.fixture
def category():
    """Создаёт тестовую категорию и сбрасывает счётчики после теста."""
    # Сбрасываем счётчики перед каждым тестом
    Category.category_count = 0
    Category.product_count = 0
    # Создаём категорию
    products = ["Product1", "Product2"]
    return Category("Electronics", "Category for electronic items", products)


# Фикстура для создания пустой категории
@pytest.fixture
def empty_category():
    """Создаёт категорию с пустым списком продуктов."""
    Category.category_count = 0
    Category.product_count = 0
    return Category("Books", "Category for books", [])


@pytest.fixture
def product_phone():
    """Фикстура для создания продукта Phone"""
    return Product(name="Phone", description="Smartphone", price=50000.0, quantity=10)


@pytest.fixture
def product_laptop():
    """Фикстура для создания продукта Laptop"""
    return Product(
        name="Laptop", description="Portable computer", price=80000.0, quantity=5
    )


@pytest.fixture
def product_phone_duplicate_higher_price():
    """Фикстура для создания дубликата Phone с более высокой ценой"""
    return Product(
        name="Phone", description="Updated smartphone", price=60000.0, quantity=3
    )


@pytest.fixture
def product_phone_duplicate_lower_price():
    """Фикстура для создания дубликата Phone с более низкой ценой"""
    return Product(
        name="Phone", description="Budget smartphone", price=40000.0, quantity=7
    )


@pytest.fixture
def category_electronics(product_phone, product_laptop):
    """Фикстура для создания категории Electronics с двумя продуктами"""
    return Category(
        name="Electronics",
        description="Devices and gadgets",
        products=[product_phone, product_laptop],
    )


@pytest.fixture
def empty_category():
    """Фикстура для создания пустой категории"""
    return Category(name="Empty", description="No products", products=[])


def test_category(empty_category):
    assert str(empty_category) == 'Empty, количество продуктов: 0 шт.'

#
# # Тест инициализации категории
# def test_category_initialization(category_electronics, product_phone, product_laptop):
#     """Проверяет корректность инициализации атрибутов категории."""
#     assert category_electronics == "Electronics"
#     assert category_electronics.description == "Category for electronic items"
#     assert category_electronics.products == [product_phone, product_laptop]
#
# # Тест счётчика продуктов
# def test_product_count(category):
#     """Проверяет корректность подсчёта продуктов."""
#     assert Category.product_count == 2
#
#
# # Тест пустой категории
# def test_empty_category(empty_category):
#     """Проверяет категорию с пустым списком продуктов."""
#     assert empty_category.name == "Books"
#     assert empty_category.description == "Category for books"
#     assert empty_category.products == []
#     assert Category.product_count == 0
#     assert Category.category_count == 1
# def test_category(empty_category):
#     pass