import pytest

from src.category import Category, CategoryIterator


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
