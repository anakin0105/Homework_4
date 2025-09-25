import pytest

from src.category import Category, CategoryIterator
from src.exceptions import ZeroQuantityError
from src.product import Product


@pytest.fixture
def category_products():
    return Category(
        "Напитки",
        "Здесь находится описание категории",
        ["молоко", "вода", "вино", "сок"],
    )


@pytest.fixture
def category_products1():
    return Category(
        "Телефоны",
        "Здесь находится описание категории",
        ["IPhone", "Samsung", "Honor", "Xiomi"],
    )


@pytest.fixture
def category_products2():
    return Category(
        "Ноутбуки",
        "Здесь находится описание категории",
        ["Asus", "MSI", "Dell", "Sony"],
    )

@pytest.fixture
def product_phone():
    """Фикстура для создания продукта Phone"""
    return Product(name="Phone", description="Smartphone", price=50000.0, quantity=10)


@pytest.fixture
def product_laptop():
    """Фикстура для создания продукта Laptop"""
    return Product(name="Laptop", description="Portable computer", price=80000.0, quantity=5)


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

@pytest.fixture
def empty_category():
    """Фикстура для создания пустой категории."""
    return Category("Test Category", "Test description", [])

@pytest.fixture
def valid_product():
    """Фикстура для продукта с положительным количеством."""
    return Product("Valid Product", "Description", 10, 100.0)

@pytest.fixture
def zero_quantity_product():
    """Фикстура для продукта с нулевым количеством."""
    return Product("Zero Quantity Product", "Description", 0, 100.0)

@pytest.fixture
def negative_quantity_product():
    """Фикстура для продукта с отрицательным количеством."""
    return Product("Negative Quantity Product", "Description", -5, 100.0)

def test_init_category(category_products):
    assert category_products.name == "Напитки"
    assert category_products.description == "Здесь находится описание категории"
    assert category_products.products == "молоко\nвода\nвино\nсок\n"


def test_counting(category_products):
    assert len(category_products.products) == 21


def test_iterator_category(category_products1, category_products2):
    cat_itr = CategoryIterator(category_products1)
    list_tel = ["IPhone", "Samsung", "Honor", "Xiomi"]
    for index, product in enumerate(cat_itr):
        assert product == list_tel[index]

def test_category_average_price(category_electronics):
    """Проверка среднего ценника при наличии товаров"""
    assert category_electronics.average_price() == (50000.0 + 80000.0) / 2  # 65000.0

def test_category_average_price_empty(empty_category):
    """Проверка среднего ценника при пустой категории"""
    assert empty_category.average_price() == 0

# Тесты для метода add_product
def test_add_product_success(empty_category, valid_product, capsys):
    """Проверка успешного добавления продукта с положительным количеством."""
    empty_category.add_product(valid_product)
    assert valid_product in empty_category.products_list()
    assert len(empty_category.products_list()) == 1
    captured = capsys.readouterr()
    assert "Товар Valid Product добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out

def test_add_product_zero_quantity(empty_category, zero_quantity_product, capsys):
    """Проверка ошибки при добавлении продукта с нулевым количеством."""
    with pytest.raises(ZeroQuantityError, match="Товар с нулевым количеством не может быть добавлен"):
        empty_category.add_product(zero_quantity_product)
    assert len(empty_category.products_list()) == 0
    captured = capsys.readouterr()
    assert "Ошибка: Товар с нулевым количеством не может быть добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out
    assert "Товар Zero Quantity Product добавлен" not in captured.out

def test_add_product_negative_quantity(empty_category, negative_quantity_product, capsys):
    """Проверка ошибки при добавлении продукта с отрицательным количеством."""
    with pytest.raises(ZeroQuantityError, match="Товар с нулевым количеством не может быть добавлен"):
        empty_category.add_product(negative_quantity_product)
    assert len(empty_category.products_list()) == 0
    captured = capsys.readouterr()
    assert "Ошибка: Товар с нулевым количеством не может быть добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out
    assert "Товар Negative Quantity Product добавлен" not in captured.out
