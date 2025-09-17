from unittest.mock import patch

import pytest

from src.product import LawnGrass, Product, Smartphone
from src.сategory import Category

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
    assert str(product_phone) == "Phone, 50000.0 руб. Остаток: 10 шт."
    assert product_phone.name == "Phone"
    assert product_phone.description == "Smartphone"
    assert product_phone.price == 50000.0
    assert product_phone.quantity == 10


def test_product_type(product_phone, empty_category):
    with pytest.raises(TypeError):
        product_phone + empty_category


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
    assert "Цена не должна быть нулевая или отрицательная!" in captured.out
    assert product_phone.price == 50000.0


def test_product_price_private_access(product_phone):
    """Тест приватности атрибута __price"""
    with pytest.raises(AttributeError):
        product_phone.__price
    assert product_phone._Product__price == 50000.0  # Проверка через манглинг


def test_category(empty_category):
    assert str(empty_category) == "Empty, количество продуктов: 0 шт."


def test_add():
    """Тест сложения двух товаров"""
    product1 = {
        "name": "Телефон",
        "description": "Смартфон",
        "price": 10000.0,
        "quantity": 2,
    }
    product2 = {
        "name": "Ноутбук",
        "description": "Игровой ноутбук",
        "price": 50000.0,
        "quantity": 1,
    }

    # Ожидаемый результат: (10000 * 2) + (50000 * 1) = 20000 + 50000 = 70000
    expected = 70000.0

    # Создаем объекты и тестируем сложение
    prod1 = Product.new_product(product1)
    prod2 = Product.new_product(product2)
    result = prod1 + prod2

    assert result == expected


# Фикстуры
@pytest.fixture
def smartphone_info():
    return {
        "name": "iPhone 14",
        "description": "Смартфон Apple",
        "price": 79990.0,
        "quantity": 10,
        "efficiency": 3.5,
        "model": "A2882",
        "memory": 128,
        "color": "Midnight Black",
    }


@pytest.fixture
def smartphone(smartphone_info):
    return Smartphone(
        name=smartphone_info["name"],
        description=smartphone_info["description"],
        quantity=smartphone_info["quantity"],
        price=smartphone_info["price"],
        efficiency=smartphone_info["efficiency"],
        model=smartphone_info["model"],
        memory=smartphone_info["memory"],
        color=smartphone_info["color"],
    )


@pytest.fixture
def smartphone2():
    return Smartphone(
        name="Samsung S23",
        description="Смартфон Samsung",
        quantity=5,
        price=65000.0,
        efficiency=3.2,
        model="S23",
        memory=256,
        color="Silver",
    )


@pytest.fixture
def lawn_grass_info():
    return {
        "name": "Green Lawn",
        "description": "Газонная трава для сада",
        "price": 1500.0,
        "quantity": 50,
        "country": "Germany",
        "germination_period": "7-14 дней",
        "color": "Green",
    }


@pytest.fixture
def lawn_grass(lawn_grass_info):
    return LawnGrass(
        name=lawn_grass_info["name"],
        description=lawn_grass_info["description"],
        quantity=lawn_grass_info["quantity"],
        price=lawn_grass_info["price"],
        country=lawn_grass_info["country"],
        germination_period=lawn_grass_info["germination_period"],
        color=lawn_grass_info["color"],
    )


@pytest.fixture
def lawn_grass2():
    return LawnGrass(
        name="Eco Grass",
        description="Экологичная трава",
        quantity=20,
        price=1200.0,
        country="Netherlands",
        germination_period="5-10 дней",
        color="Dark Green",
    )


@pytest.fixture
def product():
    return Product(
        name="Generic Product", description="Обычный продукт", quantity=5, price=1000.0
    )


# Тесты для Smartphone
def test_smartphone_init(smartphone, smartphone_info):
    """Проверка инициализации Smartphone"""
    assert smartphone.name == smartphone_info["name"]
    assert smartphone.description == smartphone_info["description"]
    assert smartphone.price == smartphone_info["price"]
    assert smartphone.quantity == smartphone_info["quantity"]
    assert smartphone.efficiency == smartphone_info["efficiency"]
    assert smartphone.model == smartphone_info["model"]
    assert smartphone.memory == smartphone_info["memory"]
    assert smartphone.color == smartphone_info["color"]


def test_smartphone_new_product(smartphone_info):
    """Проверка создания Smartphone через new_product"""
    smartphone = Smartphone.new_product(smartphone_info)
    assert smartphone.name == smartphone_info["name"]
    assert smartphone.description == smartphone_info["description"]
    assert smartphone.price == smartphone_info["price"]
    assert smartphone.quantity == smartphone_info["quantity"]
    assert smartphone.efficiency == smartphone_info["efficiency"]
    assert smartphone.model == smartphone_info["model"]
    assert smartphone.memory == smartphone_info["memory"]
    assert smartphone.color == smartphone_info["color"]


def test_smartphone_str(smartphone):
    """Проверка метода __str__ для Smartphone"""
    expected = (
        f"{smartphone.name} ({smartphone.model}, {smartphone.color}), {smartphone.price} руб. "
        f"Остаток: {smartphone.quantity} шт., Память: {smartphone.memory} ГБ, Производительность: {smartphone.efficiency}"
    )
    assert str(smartphone) == expected


def test_smartphone_add_same_class(smartphone, smartphone2):
    """Проверка успешного сложения двух объектов Smartphone"""
    total = smartphone + smartphone2
    assert total == 79990.0 * 10 + 65000.0 * 5


def test_smartphone_add_lawn_grass(smartphone, lawn_grass):
    """Проверка ошибки при сложении Smartphone с LawnGrass"""
    with pytest.raises(
        TypeError, match="Можно складывать только объекты класса Smartphone"
    ):
        smartphone + lawn_grass


def test_smartphone_add_product(smartphone, product):
    """Проверка ошибки при сложении Smartphone с Product"""
    with pytest.raises(
        TypeError, match="Можно складывать только объекты класса Smartphone"
    ):
        smartphone + product


def test_smartphone_add_invalid_type(smartphone):
    """Проверка ошибки при сложении Smartphone с некорректным типом"""
    with pytest.raises(
        TypeError, match="Можно складывать только объекты класса Smartphone"
    ):
        smartphone + "not a product"


# Тесты для LawnGrass
def test_lawn_grass_init(lawn_grass, lawn_grass_info):
    """Проверка инициализации LawnGrass"""
    assert lawn_grass.name == lawn_grass_info["name"]
    assert lawn_grass.description == lawn_grass_info["description"]
    assert lawn_grass.price == lawn_grass_info["price"]
    assert lawn_grass.quantity == lawn_grass_info["quantity"]
    assert lawn_grass.country == lawn_grass_info["country"]
    assert lawn_grass.germination_period == lawn_grass_info["germination_period"]
    assert lawn_grass.color == lawn_grass_info["color"]


def test_lawn_grass_new_product(lawn_grass_info):
    """Проверка создания LawnGrass через new_product"""
    lawn_grass = LawnGrass.new_product(lawn_grass_info)
    assert lawn_grass.name == lawn_grass_info["name"]
    assert lawn_grass.description == lawn_grass_info["description"]
    assert lawn_grass.price == lawn_grass_info["price"]
    assert lawn_grass.quantity == lawn_grass_info["quantity"]
    assert lawn_grass.country == lawn_grass_info["country"]
    assert lawn_grass.germination_period == lawn_grass_info["germination_period"]
    assert lawn_grass.color == lawn_grass_info["color"]


def test_lawn_grass_str(lawn_grass):
    """Проверка метода __str__ для LawnGrass"""
    expected = (
        f"{lawn_grass.name} ({lawn_grass.country}, {lawn_grass.color}), {lawn_grass.price} руб. "
        f"Остаток: {lawn_grass.quantity} шт., Срок прорастания: {lawn_grass.germination_period}"
    )
    assert str(lawn_grass) == expected


def test_lawn_grass_add_same_class(lawn_grass, lawn_grass2):
    """Проверка успешного сложения двух объектов LawnGrass"""
    total = lawn_grass + lawn_grass2
    assert total == 1500.0 * 50 + 1200.0 * 20


def test_lawn_grass_add_smartphone(lawn_grass, smartphone):
    """Проверка ошибки при сложении LawnGrass с Smartphone"""
    with pytest.raises(
        TypeError, match="Можно складывать только объекты класса LawnGrass"
    ):
        lawn_grass + smartphone


def test_lawn_grass_add_product(lawn_grass, product):
    """Проверка ошибки при сложении LawnGrass с Product"""
    with pytest.raises(
        TypeError, match="Можно складывать только объекты класса LawnGrass"
    ):
        lawn_grass + product


def test_lawn_grass_add_invalid_types(lawn_grass):
    """Проверка ошибки при сложении LawnGrass с некорректным типом"""
    with pytest.raises(
        TypeError, match="Можно складывать только объекты класса LawnGrass"
    ):
        lawn_grass + "not a product"
