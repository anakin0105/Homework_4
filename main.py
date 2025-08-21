from src.Category_class import Category  # Импортируем класс Category
from src.Product_class import Product
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
