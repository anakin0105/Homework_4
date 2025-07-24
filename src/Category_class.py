class Category:
    """Класс Category с атрибутом: название, описание,
    лист продуктов, количество категорий, количество товаров"""

    name: str  # атрибут: название
    description: str  # атрибут: описание
    products: list  # атрибут: лист продуктов
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод __init__ для Класса Category"""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)


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
