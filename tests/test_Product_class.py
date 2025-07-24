import pytest

from src.Product_class import Product


@pytest.fixture
def product():
    """Фикстура для создания экземпляра класса Product."""
    return Product(name="Apple", description="Fresh red apple", price=1.99, quantity=10)


def test_product_initialization(product):
    """Проверка корректности инициализации объекта Product."""
    assert product.name == "Apple"
    assert product.description == "Fresh red apple"
    assert product.price == 1.99
    assert product.quantity == 10


def test_product_types():
    """Проверка типов атрибутов объекта Product."""
    product = Product(
        name="Apple", description="Fresh red apple", price=1.99, quantity=10
    )
    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)
