class Product: #
    """ Класс Product с атрибутом: название, описание, цена, количество"""
    name: str #атрибут: название
    description: str #атрибут: описание
    price: float #атрибут: цена
    quantity: int #атрибут: количество

    def __init__(self, name, description, price, quantity):
        """Метод __init__ для Класса Product"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity