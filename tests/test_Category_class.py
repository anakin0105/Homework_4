
import pytest
from unittest.mock import patch
from main import Category, Product # Предполагается, что классы в файле main.py

# Фикстуры для создания тестовых данных

@pytest.fixture
def product_phone():
 """Фикстура для создания продукта Phone"""
 return Product(name="Phone", description="Smartphone", price=50000.0, quantity=10)

@pytest.fixture
def product_laptop():
 """Фикстура для создания продукта Laptop"""
 return Product(name="Laptop", description="Portable computer", price=80000.0, quantity=5)

@pytest.fixture
def product_phone_duplicate_higher_price():
 """Фикстура для создания дубликата Phone с более высокой ценой"""
 return Product(name="Phone", description="Updated smartphone", price=60000.0, quantity=3)

@pytest.fixture
def product_phone_duplicate_lower_price():
 """Фикстура для создания дубликата Phone с более низкой ценой"""
 return Product(name="Phone", description="Budget smartphone", price=40000.0, quantity=7)

@pytest.fixture
def category_electronics(product_phone, product_laptop):
 """Фикстура для создания категории Electronics с двумя продуктами"""
 return Category(name="Electronics", description="Devices and gadgets", products=[product_phone, product_laptop])

@pytest.fixture
def empty_category():
 """Фикстура для создания пустой категории"""
 return Category(name="Empty", description="No products", products=[])

# Тесты для класса Category
def test_category_init(category_electronics):
    """Тест инициализации категории"""
    assert category_electronics.name == "Electronics"
    assert category_electronics.description == "Devices and gadgets"
    assert len(category_electronics._Category__products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2

def test_category_products_getter(category_electronics):
    """Тест геттера products"""
    expected_output = (
        "Phone, 50000.0 руб. Остаток: 10 шт.\n"
        "Laptop, 80000.0 руб. Остаток: 5 шт.\n"
    )
    assert category_electronics.products == expected_output

def test_category_add_product_unique(category_electronics, product_tablet):
    """Тест добавления уникального продукта"""
    category_electronics.add_product(product_tablet)
    assert len(category_electronics._Category__products) == 3
    assert Category.product_count == 3
    assert product_tablet in category_electronics._Category__products

@patch('builtins.input', return_value='y')
def test_category_add_product_duplicate_higher_price(mock_input, category_electronics, product_phone_duplicate_higher_price):
    """Тест добавления дубликата с более высокой ценой"""
    category_electronics.add_product(product_phone_duplicate_higher_price)
    assert len(category_electronics._Category__products) == 2
    assert Category.product_count == 2
    phone = category_electronics._Category__products[0]
    assert phone.quantity == 13  # 10 + 3
    assert phone.price == 60000.0  # max(50000, 60000)

@patch('builtins.input', return_value='y')
def test_category_add_product_duplicate_lower_price_confirm(mock_input, category_electronics, product_phone_duplicate_lower_price):
    """Тест добавления дубликата с более низкой ценой (подтверждение)"""
    category_electronics.add_product(product_phone_duplicate_lower_price)
    assert len(category_electronics._Category__products) == 2
    assert Category.product_count == 2
    phone = category_electronics._Category__products[0]
    assert phone.quantity == 17  # 10 + 7
    assert phone.price == 40000.0  # Пользователь подтвердил понижение

@patch('builtins.input', return_value='n')
def test_category_add_product_duplicate_lower_price_cancel(mock_input, category_electronics, product_phone_duplicate_lower_price):
    """Тест добавления дубликата с более низкой ценой (отказ)"""
    category_electronics.add_product(product_phone_duplicate_lower_price)
    assert len(category_electronics._Category__products) == 2
    assert Category.product_count == 2
    phone = category_electronics._Category__products[0]
    assert phone.quantity == 17  # 10 + 7
    assert phone.price == 50000.0  # Пользователь отказался от понижения

def test_category_add_product_invalid_type(category_electronics):
    """Тест добавления неверного типа продукта"""
    with pytest.raises(ValueError, match="Можно добавлять только объекты класса Product"):
        category_electronics.add_product("Not a Product")

def test_category_products_private_access(category_electronics):
    """Тест приватности атрибута __products"""
    with pytest.raises(AttributeError):
        category_electronics.__products
    assert len(category_electronics._Category__products) == 2  # Проверка через манглинг