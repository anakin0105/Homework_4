import pytest

from src.category import Category
from src.exceptions import ZeroQuantityError
from src.product import Product
from src.order import Order


@pytest.fixture
def product():
    return Product("Phone", "Smartphone", 10, 50000.0)


@pytest.fixture
def order(product):
    return Order("Order1", "Тестовый заказ", product, 2)


def test_order_init(order, product):
    """Проверка инициализации Order."""
    assert order.name == "Order1"
    assert order.description == "Тестовый заказ"
    assert order.product == product
    assert order.quantity == 2
    assert order.total_price == 50000.0 * 2


def test_order_str(order):
    """Проверка метода __str__ для Order."""
    assert (
        str(order)
        == "Заказ: Order1, Товар: Phone, Количество: 2, Итоговая стоимость: 100000.0 руб."
    )


def test_order_invalid_product():
    """Проверка ошибки при передаче некорректного товара."""
    with pytest.raises(
        TypeError,
        match="Товар должен быть экземпляром класса, наследующего BaseProduct",
    ):
        Order("Order1", "Тестовый заказ", "not a product", 2)

