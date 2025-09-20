from abc import ABC, abstractmethod


class PrintInitMixin:
    def __init__(self, *args, **kwargs):
        print(
            f"Создан объект класса {self.__class__.__name__} с параметрами: {repr(args)}, {kwargs}"
        )
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, quantity: int, price: float):
        self.name = name
        self.description = description
        self.quantity = quantity
        self._price = price

    @classmethod
    @abstractmethod
    def new_product(cls, product_info):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(PrintInitMixin, BaseProduct):  #
    """Класс Product с атрибутом: название, описание, цена, количество"""

    name: str  # атрибут: название
    description: str  # атрибут: описание
    price: float  # атрибут: цена
    quantity: int  # атрибут: количество

    def __init__(self, name: str, description: str, quantity: int, price: float):
        super().__init__(name, description, quantity, price)
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = price

    @classmethod
    def new_product(cls, product_info):
        return cls(
            name=product_info["name"],
            description=product_info["description"],
            price=product_info["price"],
            quantity=product_info["quantity"],
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
            if confirmation != "y":
                print("Понижение цены отменено.")
                return
        self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Тип данных должен быть Product")
        return self.__price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """Класс Smartphone, наследник Product, с дополнительными атрибутами: производительность, модель, объем памяти, цвет"""

    def __init__(
        self,
        name: str,
        description: str,
        quantity: int,
        price: float,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, quantity, price)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    @classmethod
    def new_product(cls, product_info):
        return cls(
            name=product_info["name"],
            description=product_info["description"],
            price=product_info["price"],
            quantity=product_info["quantity"],
            efficiency=product_info["efficiency"],
            model=product_info["model"],
            memory=product_info["memory"],
            color=product_info["color"],
        )

    def __str__(self):
        return (
            f"{self.name} ({self.model}, {self.color}), {self.price} руб. "
            f"Остаток: {self.quantity} шт., Память: {self.memory} ГБ, Производительность: {self.efficiency}"
        )

    def __add__(self, other):
        if not isinstance(other, Smartphone):
            raise TypeError("Можно складывать только объекты класса Smartphone")
        return self.price * self.quantity + other.price * other.quantity


class LawnGrass(Product):
    """Класс LawnGrass, наследник Product, с дополнительными атрибутами: страна-производитель, срок прорастания, цвет"""

    def __init__(
        self,
        name: str,
        description: str,
        quantity: int,
        price: float,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, quantity, price)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    @classmethod
    def new_product(cls, product_info):
        return cls(
            name=product_info["name"],
            description=product_info["description"],
            price=product_info["price"],
            quantity=product_info["quantity"],
            country=product_info["country"],
            germination_period=product_info["germination_period"],
            color=product_info["color"],
        )

    def __str__(self):
        return (
            f"{self.name} ({self.country}, {self.color}), {self.price} руб. "
            f"Остаток: {self.quantity} шт., Срок прорастания: {self.germination_period}"
        )

    def __add__(self, other):
        if not isinstance(other, LawnGrass):
            raise TypeError("Можно складывать только объекты класса LawnGrass")
        return self.price * self.quantity + other.price * other.quantity


# # Пример использования:
# if __name__ == "__main__":
#     smartphone = Smartphone(
#         name="iPhone 14",
#         description="Смартфон Apple",
#         quantity=10,
#         price=79990.0,
#         efficiency=3.5,
#         model="A2882",
#         memory=128,
#         color="Midnight Black"
#     )
#     smartphone2 = Smartphone(
#         name="Samsung S23",
#         description="Смартфон Samsung",
#         quantity=5,
#         price=65000.0,
#         efficiency=3.2,
#         model="S23",
#         memory=256,
#         color="Silver"
#     )
#     lawn_grass = LawnGrass(
#         name="Green Lawn",
#         description="Газонная трава для сада",
#         quantity=50,
#         price=1500.0,
#         country="Germany",
#         germination_period="7-14 дней",
#         color="Green"
#     )
#     product = Product(
#         name="Generic Product",
#         description="Обычный продукт",
#         quantity=5,
#         price=1000.0
#     )
#
#     # Успешное сложение
#     total_smartphones = smartphone + smartphone2
#     print(f"Общая стоимость смартфонов: {total_smartphones} руб.")  # Работает
#
#     # Ошибка при сложении Smartphone с LawnGrass
#     try:
#         smartphone + lawn_grass
#     except TypeError as e:
#         print(f"Ошибка: {e}")
#
#     # Ошибка при сложении Smartphone с Product
#     try:
#         smartphone + product
#     except TypeError as e:
#         print(f"Ошибка: {e}")
#
#     # Ошибка при сложении Smartphone с некорректным типом
#     try:
#         smartphone + "not a product"
#     except TypeError as e:
#         print(f"Ошибка: {e}")


# # Пример использования:
# if __name__ == "__main__":
#     # Создаем смартфон
#     smartphone_info = {
#         "name": "iPhone 14",
#         "description": "Смартфон Apple",
#         "price": 79990.0,
#         "quantity": 10,
#         "efficiency": 3.5,
#         "model": "A2882",
#         "memory": 128,
#         "color": "Midnight Black"
#     }
#     smartphone = Smartphone.new_product(smartphone_info)
#     print(smartphone)
#
#     # Создаем газонную траву
#     lawn_grass_info = {
#         "name": "Green Lawn",
#         "description": "Газонная трава для сада",
#         "price": 1500.0,
#         "quantity": 50,
#         "country": "Germany",
#         "germination_period": "7-14 дней",
#         "color": "Green"
#     }
#     lawn_grass = LawnGrass.new_product(lawn_grass_info)
#     print(lawn_grass)
#
#     # Проверяем сумму
#     total = smartphone + lawn_grass
#     print(f"Общая стоимость: {total} руб.")
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
