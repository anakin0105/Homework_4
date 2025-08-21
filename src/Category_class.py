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

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

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
        if not isinstance(product, Product):  # Проверка, что product — объект Product
            raise ValueError("Можно добавлять только объекты класса Product")

        for existing_product in self.__products:
            if existing_product == product.name:
                existing_product.quantity += product.quantity
                # Выбираем более высокую цену
                new_price = max(existing_product.price, product.price)
                existing_product.price = new_price
                return
        self.__products.append(product)
        Category.product_count += 1

    def __iter__(self):
        return CategoryIterator(self)


class CategoryIterator:
    def __init__(self, category):
        self.products = category.products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        raise StopIteration


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
