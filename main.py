from src.category import Category  # Импортируем класс Category
from src.product import Product, Smartphone
from src.utils import read_json_file

if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 0, 1000.0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print(
            "Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством"
        )

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )

    print(
        f"Средняя цена в категории '{category1.name}': {category1.average_price()} руб."
    )

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(
        f"Средняя цена в категории '{category_empty.name}': {category_empty.average_price()} руб."
    )

# def main():
#     data = read_json_file("data/products.json")
#     for category_data in data:
#         products = []
#         for p in category_data["products"]:
#             if "efficiency" in p:  # Проверка на смартфон
#                 product = Smartphone.new_product(p)
#             else:
#                 product = Product.new_product(p)
#             products.append(product)
#         category = Category(category_data["name"], category_data["description"], products)
#         print(f"Категория: {category.name}, Средняя цена: {category.average_price()}")
#         # Тестируем добавление товара
#         try:
#             invalid_product = Product("Invalid", "Test", 0, 100.0)
#             category.add_product(invalid_product)
#         except ValueError:
#             pass  # Ошибка обрабатывается в add_product
#         category.add_product(Product("Test Product", "Description", 10, 200.0))
#
#
# if __name__ == "__main__":
#     main()


# if __name__ == "__main__":
#     product1 = Product(
#         "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
#     )
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
#
#     print(product3.name)
#     print(product3.description)
#     print(product3.price)
#     print(product3.quantity)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3],
#     )
#
#     print(category1.name == "Смартфоны")
#     print(category1.description)
#     print(len(category1.products))
#     print(category1.category_count)
#     print(category1.product_count)
#
#     product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
#     category2 = Category(
#         "Телевизоры",
#         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#         [product4],
#     )
#
#     print(category2.name)
#     print(category2.description)
#     print(len(category2.products))
#     print(category2.products)
#
#     print(Category.category_count)
#     print(Category.product_count)
# def main() -> list:
#     """
#     Читает данные из JSON-файла с помощью read_json_file и создаёт объекты Category и Product.
#
#     Returns:
#         list: Список объектов Category с товарами.
#     """
#     # Читаем данные из JSON
#     data = read_json_file(PATH_TO_FILE)
#     print(f"Данные из JSON: {data}")
#     print(read_json_file(PATH_TO_FILE))
#
#     categories_main = []
#     for category_data in data:
#         try:
#             # Создаём список объектов Product
#             products = [
#                 Product(
#                     name=prod["name"],
#                     description=["description"],
#                     price=prod["price"],
#                     quantity=prod["quantity"],
#                 )
#                 for prod in category_data["products"]
#             ]
#             # Создаём объект Category
#             category_main = Category(
#                 name=category_data["name"],
#                 description=category_data["description"],
#                 products=products,
#             )
#             categories_main.append(category_main)
#         except KeyError as e:
#             print(f"Ошибка: В JSON отсутствует ключ {e}")
#             continue
#
#     return categories_main
#
#
# if __name__ == "__main__":
#     # Вызываем main и выводим результат для проверки
#     categories = main()
#     for category in categories:
#         print(f"Категория: {category.name}, Описание: {category.description}")
#         print("Товары:")
#         for product in category.products:
#             print(
#                 f"  - {product.name}: Цена = {product.price}, Количество = {product.quantity}"
#             )
#         print()
#     # Код проверки для демонстрации дополнительного задания 3
#     # 1. Создаём продукты для тестирования
#     product1 = Product(
#         name="Phone", description="Smartphone", price=50000.0, quantity=10
#     )  # Первый продукт
#     product2 = Product(
#         name="Laptop", description="Portable computer", price=80000.0, quantity=5
#     )  # Уникальный продукт
#     product3 = Product(
#         name="Phone", description="Updated smartphone", price=60000.0, quantity=3
#     )  # Дубликат Phone с более высокой ценой
#     product4 = Product(
#         name="Phone", description="Budget smartphone", price=40000.0, quantity=7
#     )  # Дубликат Phone с более низкой ценой
#     product5 = Product(
#         name="Tablet", description="Touchscreen device", price=30000.0, quantity=8
#     )  # Уникальный продукт
#     # 2. Создаём категорию с начальными продуктами
#     category = Category(
#         name="Electronics",
#         description="Devices and gadgets",
#         products=[product1, product2],  # Начинаем с Phone и Laptop
#     )
#     print("Начальное состояние категории:")  # Показываем начальное состояние
#     print(f"Категория: {category.name}, Описание: {category.description}")
#     print("Продукты:")
#     print(
#         category.products
#     )  # Ожидается: Phone (50000.0, 10 шт.), Laptop (80000.0, 5 шт.)
#     print(f"Всего категорий: {Category.category_count}")  # Ожидается: 1
#     print(f"Всего продуктов: {Category.product_count}")  # Ожидается: 2
#
#     # 3. Добавляем уникальный продукт (Tablet)
#     category.add_product(product5)
#     print("\nПосле добавления Tablet (уникальный продукт):")
#     print(category.products)  # Ожидается: Phone, Laptop, Tablet
#     print(f"Всего продуктов: {Category.product_count}")  # Ожидается: 3
#
#     # 4. Добавляем дубликат Phone с более высокой ценой (60000.0)
#     category.add_product(product3)
#     print("\nПосле добавления дубликата Phone (цена 60000.0):")
#     print(category.products)  # Ожидается: Phone (60000.0, 13 шт.), Laptop, Tablet
#     print(
#         f"Всего продуктов: {Category.product_count}"
#     )  # Ожидается: 3 (дубликат не увеличивает счётчик)
#
#     # 5. Добавляем дубликат Phone с более низкой ценой (40000.0, требует подтверждения)
#     print("\nДобавление дубликата Phone с более низкой ценой (40000.0):")
#     category.add_product(product4)  # Запросит подтверждение, так как цена понижается
#     print(
#         category.products
#     )  # Если ввести 'y': Phone (40000.0, 20 шт.), если 'n': Phone (60000.0, 20 шт.)
#     print(f"Всего продуктов: {Category.product_count}")  # Ожидается: 3
#
#     # 6. Проверяем сеттер цены напрямую для демонстрации
#     print("\nПроверка изменения цены Phone напрямую:")
#     product1.price = 70000.0  # Повышение цены, подтверждение не требуется
#     print(f"Новая цена Phone: {product1.price}")  # Ожидается: 70000.0
#     print(category.products)  # Ожидается: Phone (70000.0, 20 шт.), Laptop, Tablet
