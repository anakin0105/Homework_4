
from src.Product_class import Product



class Category:
    """Класс Category с атрибутом: название, описание,
    лист продуктов, количество категорий, количество товаров."""

    category_number = 0
    product_amount = 0
    name: str  # атрибут: название
    description: str  # атрибут: описание
    products: list  # атрибут: лист продуктов
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод __init__ для Класса Category."""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        product_str = " "
        for product in self.__products:
            product_str += f"Название продукта {product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    def add_product(self, product):
        """
        Метод для добавления продукта в приватный список _products.
        Требование Задания 1: принимает объект Product, добавляет в _products через append,
        ничего не возвращает.
        Требование задания 14.2: увеличивает product_count на 1.
        """
        if isinstance(product, Product):  # Проверка, что product — объект Product
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Можно добавлять только объекты класса Product")


# # Примеры использования
# # 1. Создаём несколько категорий
# category1 = Category(
#     name="Electronics",
#     description="Devices and gadgets",
#     products=["Phone", "Laptop", "Tablet"]
# )
#
# category2 = Category(
#     name="Books",
#     description="Fiction and non-fiction books",
#     products=["Novel", "Textbook"]
# )
#
#
# # 2. Проверяем атрибуты экземпляров
# print(f"Category 1: {category1.name}, Description: {category1.description}, Products: {category1.products}")
# # Вывод: Category 1: Electronics, Description: Devices and gadgets, Products: ['Phone', 'Laptop', 'Tablet']
#
# print(f"Category 2: {category2.name}, Description: {category2.description}, Products: {category2.products}")
# # Вывод: Category 2: Books, Description: Fiction and non-fiction books, Products: ['Novel', 'Textbook']
#
# # 3. Проверяем статические переменные
# print(f"Total categories: {Category.category_number}")
# # Вывод: Total categories: 2
#
# print(f"Total products across all categories: {Category.product_amount}")
# # Вывод: Total products across all categories: 5
#
# # 4. Добавляем продукт в категорию
# category1.products.append("Headphones")
# Category.product_amount += 1  # Обновляем общее количество продуктов
# print(f"Updated products in {category1.name}: {category1.products}")
# # Вывод: Updated products in Electronics: ['Phone', 'Laptop', 'Tablet', 'Headphones']
# print(f"Total products now: {Category.product_amount}")
# # Вывод: Total products now: 6
#
# # Примеры использования
# # 1. Создаём несколько продуктов
# product1 = Product(name="Phone", description="Smartphone", price=50000.0, quantity=10)
# product2 = Product(name="Laptop", description="Portable computer", price=80000.0, quantity=5)
# product3 = Product(name="Tablet", description="Touchscreen device", price=30000.0, quantity=8)
# product4 = Product(name="Novel", description="Fiction book", price=1000.0, quantity=20)
# product5 = Product(name="Textbook", description="Educational book", price=2000.0, quantity=15)
#
# # 2. Создаём несколько категорий с объектами Product
# category1 = Category(
#     name="Electronics",
#     description="Devices and gadgets",
#     products=[product1, product2, product3]  # ✅ Исправлено: передаём список объектов Product вместо строк
# )
#
# category2 = Category(
#     name="Books",
#     description="Fiction and non-fiction books",
#     products=[product4, product5]  # ✅ Исправлено: передаём список объектов Product вместо строк
# )
#
# # 3. Проверяем атрибуты экземпляров
# print(f"Category 1: {category1.name}, Description: {category1.description}, Products:\n{category1.products}")
# # Вывод:
# # Category 1: Electronics, Description: Devices and gadgets, Products:
# # Phone, 50000.0 руб. Остаток: 10 шт.
# # Laptop, 80000.0 руб. Остаток: 5 шт.
# # Tablet, 30000.0 руб. Остаток: 8 шт.
#
# print(f"Category 2: {category2.name}, Description: {category2.description}, Products:\n{category2.products}")
# # Вывод:
# # Category 2: Books, Description: Fiction and non-fiction books, Products:
# # Novel, 1000.0 руб. Остаток: 20 шт.
# # Textbook, 2000.0 руб. Остаток: 15 шт.
#
# # 4. Проверяем статические переменные
# print(f"Total categories: {Category.category_count}")  # ✅ Исправлено: category_number на category_count
# # Вывод: Total categories: 2
#
# print(f"Total products across all categories: {Category.product_count}")  # ✅ Исправлено: product_amount на product_count
# # Вывод: Total products across all categories: 5
#
# # 5. Добавляем продукт в категорию
# new_product = Product(name="Headphones", description="Wireless headphones", price=15000.0, quantity=12)
# category1.add_product(new_product)  # ✅ Исправлено: используем add_product вместо products.append
# print(f"Updated products in {category1.name}:\n{category1.products}")
# # Вывод:
# # Updated products in Electronics:
# # Phone, 50000.0 руб. Остаток: 10 шт.
# # Laptop, 80000.0 руб. Остаток: 5 шт.
# # Tablet, 30000.0 руб. Остаток: 8 шт.
# # Headphones, 15000.0 руб. Остаток: 12 шт.
#
# print(f"Total products now: {Category.product_count}")  # ✅ Исправлено: product_amount на product_count
# # Вывод: Total products now: 6
#
# # 6. Проверяем сеттер цены с подтверждением понижения
# print("\nПроверка изменения цены:")
# product1.price = 60000.0  # Повышение цены, подтверждение не требуется
# print(f"Новая цена Phone: {product1.price}")  # Вывод: Новая цена Phone: 60000.0
#
# product1.price = 40000.0  # Понижение цены, требуется подтверждение
# # В консоли появится: Вы уверены, что хотите понизить цену? (y/n):
# # Если ввести 'y', цена изменится, если 'n' — останется прежней
# print(f"Новая цена Phone: {product1.price}")
