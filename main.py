from src.сategory import Category  # Импортируем класс Category
from src.product import Product
from src.utils import (  # Импортируем функцию read_json_file из utils
    PATH_TO_FILE,
    read_json_file,
)


def main() -> list:
    """
    Читает данные из JSON-файла с помощью read_json_file и создаёт объекты Category и Product.

    Returns:
        list: Список объектов Category с товарами.
    """
    # Читаем данные из JSON
    data = read_json_file(PATH_TO_FILE)
    print(f"Данные из JSON: {data}")
    print(read_json_file(PATH_TO_FILE))

    categories_main = []
    for category_data in data:
        try:
            # Создаём список объектов Product
            products = [
                Product(
                    name=prod["name"],
                    description=["description"],
                    price=prod["price"],
                    quantity=prod["quantity"],
                )
                for prod in category_data["products"]
            ]
            # Создаём объект Category
            category_main = Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products,
            )
            categories_main.append(category_main)
        except KeyError as e:
            print(f"Ошибка: В JSON отсутствует ключ {e}")
            continue

    return categories_main


if __name__ == "__main__":
    # Вызываем main и выводим результат для проверки
    categories = main()
    for category in categories:
        print(f"Категория: {category.name}, Описание: {category.description}")
        print("Товары:")
        for product in category.products:
            print(
                f"  - {product.name}: Цена = {product.price}, Количество = {product.quantity}"
            )
        print()
    # Код проверки для демонстрации дополнительного задания 3
    # 1. Создаём продукты для тестирования
    product1 = Product(
        name="Phone", description="Smartphone", price=50000.0, quantity=10
    )  # Первый продукт
    product2 = Product(
        name="Laptop", description="Portable computer", price=80000.0, quantity=5
    )  # Уникальный продукт
    product3 = Product(
        name="Phone", description="Updated smartphone", price=60000.0, quantity=3
    )  # Дубликат Phone с более высокой ценой
    product4 = Product(
        name="Phone", description="Budget smartphone", price=40000.0, quantity=7
    )  # Дубликат Phone с более низкой ценой
    product5 = Product(
        name="Tablet", description="Touchscreen device", price=30000.0, quantity=8
    )  # Уникальный продукт
    # 2. Создаём категорию с начальными продуктами
    category = Category(
        name="Electronics",
        description="Devices and gadgets",
        products=[product1, product2],  # Начинаем с Phone и Laptop
    )
    print("Начальное состояние категории:")  # Показываем начальное состояние
    print(f"Категория: {category.name}, Описание: {category.description}")
    print("Продукты:")
    print(category.products)  # Ожидается: Phone (50000.0, 10 шт.), Laptop (80000.0, 5 шт.)
    print(f"Всего категорий: {Category.category_count}")  # Ожидается: 1
    print(f"Всего продуктов: {Category.product_count}")  # Ожидается: 2

    # 3. Добавляем уникальный продукт (Tablet)
    category.add_product(product5)
    print("\nПосле добавления Tablet (уникальный продукт):")
    print(category.products)  # Ожидается: Phone, Laptop, Tablet
    print(f"Всего продуктов: {Category.product_count}")  # Ожидается: 3

    # 4. Добавляем дубликат Phone с более высокой ценой (60000.0)
    category.add_product(product3)
    print("\nПосле добавления дубликата Phone (цена 60000.0):")
    print(category.products)  # Ожидается: Phone (60000.0, 13 шт.), Laptop, Tablet
    print(
        f"Всего продуктов: {Category.product_count}"
    )  # Ожидается: 3 (дубликат не увеличивает счётчик)

    # 5. Добавляем дубликат Phone с более низкой ценой (40000.0, требует подтверждения)
    print("\nДобавление дубликата Phone с более низкой ценой (40000.0):")
    category.add_product(product4)  # Запросит подтверждение, так как цена понижается
    print(
        category.products
    )  # Если ввести 'y': Phone (40000.0, 20 шт.), если 'n': Phone (60000.0, 20 шт.)
    print(f"Всего продуктов: {Category.product_count}")  # Ожидается: 3

    # 6. Проверяем сеттер цены напрямую для демонстрации
    print("\nПроверка изменения цены Phone напрямую:")
    product1.price = 70000.0  # Повышение цены, подтверждение не требуется
    print(f"Новая цена Phone: {product1.price}")  # Ожидается: 70000.0
    print(category.products)  # Ожидается: Phone (70000.0, 20 шт.), Laptop, Tablet
