from src.category import BaseEntity
from src.exceptions import ZeroQuantityError
from src.product import BaseProduct


class Order(BaseEntity):
    """Класс для заказа, содержащий один товар, количество и итоговую стоимость."""

    def __init__(
        self, name: str, description: str, product: BaseProduct, quantity: int
    ):
        super().__init__(name, description)
        try:
            if not isinstance(product, BaseProduct):
                raise TypeError(
                    "Товар должен быть экземпляром класса, наследующего BaseProduct"
                )
            if quantity <= 0:
                raise ZeroQuantityError(
                    "Товар с нулевым количеством не может быть добавлен"
                )
            self.product = product
            self.quantity = quantity
            self.total_price = product.price * quantity
            print(f"Товар {product.name} добавлен в заказ")
        except (TypeError, ZeroQuantityError) as e:
            print(f"Ошибка: {e}")
            raise
        finally:
            print("Обработка добавления товара завершена")

    def __str__(self):
        return f"Заказ: {self.name}, Товар: {self.product.name}, Количество: {self.quantity}, Итоговая стоимость: {self.total_price} руб."
