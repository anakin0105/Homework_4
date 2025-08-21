from unittest.mock import patch

import pytest

from src.Category_class import Category
from src.Product_class import Product


# Фикстуры для создания тестовых данных


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


# Тесты для класса Product
def test_product_init(product_phone):
    """Тест инициализации продукта"""
    assert product_phone.name == "Phone"
    assert product_phone.description == "Smartphone"
    assert product_phone.price == 50000.0
    assert product_phone.quantity == 10


def test_product_new_product():
    """Тест класс-метода new_product"""
    product_info = {
        "name": "Tablet",
        "description": "Touchscreen device",
        "price": 30000.0,
        "quantity": 8,
    }
    product = Product.new_product(product_info)
    assert product.name == "Tablet"
    assert product.description == "Touchscreen device"
    assert product.price == 30000.0
    assert product.quantity == 8


def test_product_price_getter(product_phone):
    """Тест геттера цены"""
    assert product_phone.price == 50000.0


def test_product_price_setter_increase(product_phone):
    """Тест сеттера цены при повышении"""
    product_phone.price = 60000.0
    assert product_phone.price == 60000.0


@patch("builtins.input", return_value="y")
def test_product_price_setter_decrease_confirm(mock_input, product_phone):
    """Тест сеттера цены при понижении с подтверждением"""
    product_phone.price = 40000.0
    assert product_phone.price == 40000.0


@patch("builtins.input", return_value="n")
def test_product_price_setter_decrease_cancel(mock_input, product_phone):
    """Тест сеттера цены при понижении с отказом"""
    product_phone.price = 40000.0
    assert product_phone.price == 50000.0


def test_product_price_setter_invalid(product_phone, capsys):
    """Тест сеттера цены при невалидной цене"""
    product_phone.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_phone.price == 50000.0


def test_product_price_private_access(product_phone):
    """Тест приватности атрибута __price"""
    with pytest.raises(AttributeError):
        product_phone.__price
    assert product_phone._Product__price == 50000.0  # Проверка через манглинг

