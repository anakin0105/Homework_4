from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """Абстрактный базовый класс для Category и Order."""

    @abstractmethod
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self):
        pass

class Category(BaseEntity):
    """
    Класс для категорий товара
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        total_products_count = sum([p.price for p in self.__products])
        return f"{self.name}, количество продуктов: {total_products_count} шт."

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += f"{product}\n"
        return result

    def products_list(self):
        return self.__products


class CategoryIterator:
    def __init__(self, category):
        self.products = category.products_list()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        raise StopIteration
