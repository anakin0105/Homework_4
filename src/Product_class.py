class Product:  #
    """Класс Product с атрибутом: название, описание, цена, количество"""

    name: str  # атрибут: название
    description: str  # атрибут: описание
    price: float  # атрибут: цена
    quantity: int  # атрибут: количество

    def __init__(self, name, description, price, quantity):
        """Метод __init__ для Класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls,product_info):
        return cls(
            name = product_info["name"],
            description = product_info["description"],
            price = product_info["price"],
            quantity = product_info["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная!")
            return
        if new_price < self.__price:
                confirmation = input("Вы уверены, что хотите понизить цену? (y/n): ")
                if confirmation != 'y':
                    print("Понижение цены отменено.")
                    return
        self.__price = new_price
# # Примеры использования класса Product
#
# # 1. Создание продукта через init
# product1 = Product(name="Phone", description="Smartphone", price=50000.0, quantity=10)
# print(f"Продукт 1: {product1.name}, Описание: {product1.description}, Цена: {product1.price}, Количество: {product1.quantity}")
# # Ожидаемый вывод: Продукт 1: Phone, Описание: Smartphone, Цена: 50000.0, Количество: 10
#
# # 2. Создание продукта через класс-метод new_product
# product_info = {
#     "name": "Laptop",
#     "description": "Portable computer",
#     "price": 80000.0,
#     "quantity": 5
# }
# product2 = Product.new_product(product_info)
# print(f"Продукт 2: {product2.name}, Описание: {product2.description}, Цена: {product2.price}, Количество: {product2.quantity}")
# # Ожидаемый вывод: Продукт 2: Laptop, Описание: Portable computer, Цена: 80000.0, Количество: 5
#
# # 3. Проверка геттера цены
# print(f"Текущая цена Phone: {product1.price}")
# # Ожидаемый вывод: Текущая цена Phone: 50000.0
#
# # 4. Проверка сеттера цены: повышение цены (не требует подтверждения)
# product1.price = 60000.0
# print(f"Новая цена Phone после повышения: {product1.price}")
# # Ожидаемый вывод: Новая цена Phone после повышения: 60000.0
#
# # 5. Проверка сеттера цены: понижение цены с подтверждением
# product1.price = 40000.0
# # Появится запрос: Вы уверены, что хотите понизить цену? (y/n):
# # Если ввести 'y':
# # Ожидаемый вывод: Новая цена Phone после понижения: 40000.0
# # Если ввести 'n' (или любой другой символ):
# # Ожидаемый вывод: Понижение цены отменено.
# #                  Новая цена Phone после понижения: 60000.0
#
# # 6. Проверка сеттера цены: невалидная цена
# product1.price = 0
# # Ожидаемый вывод: Цена не может быть нулевая или отрицательная!
# print(f"Цена Phone после попытки установить 0: {product1.price}")
# # Ожидаемый вывод: Цена Phone после попытки установить 0: 60000.0 (или 40000.0, если в шаге 5 было подтверждение)