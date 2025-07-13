import pytest

from src.Category_class import Category


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


# Тест инициализации категории
def test_category_initialization(category):
    """Проверяет корректность инициализации атрибутов категории."""
    assert category.name == "Electronics"
    assert category.description == "Category for electronic items"
    assert category.products == ["Product1", "Product2"]

# Тест счётчика продуктов
def test_product_count(category):
    """Проверяет корректность подсчёта продуктов."""
    assert Category.product_count == 2


# Тест пустой категории
def test_empty_category(empty_category):
    """Проверяет категорию с пустым списком продуктов."""
    assert empty_category.name == "Books"
    assert empty_category.description == "Category for books"
    assert empty_category.products == []
    assert Category.product_count == 0
    assert Category.category_count == 1

