import datetime


class Product:
    """Класс продукта"""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Perishable(Product):
    """Класс продукта со сроком годности"""

    def __init__(self, name, price, quantity, created_date, shelf_life):
        super().__init__(name, price, quantity)
        self.created_date = created_date
        self.shelf_life = shelf_life

    def is_expired(self):
        """Проверка на истечение срока годности"""
        current_date = datetime.datetime.now()
        expiration_date = self.created_date + datetime.timedelta(days=self.shelf_life)
        return current_date > expiration_date


class Vitamin(Product):
    """Класс витаминов"""

    def __init__(self, name, price, quantity, requires_prescription):
        super().__init__(name, price, quantity)
        self.requires_prescription = requires_prescription


class Cart:
    """Класс корзины"""

    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        """Добавление продукта в корзину"""
        if product.quantity < quantity:
            print(f"Товара {product.name} недостаточно на складе.")
        elif isinstance(product, Perishable) and product.is_expired():
            print(f"Товар {product.name} просрочен и не может быть продан.")
        elif isinstance(product, Vitamin) and product.requires_prescription:
            print(f"Витамины {product.name} нельзя продавать без рецепта.")
        else:
            self.items.append((product, quantity))

    def calculate_total(self):
        """Сумма всех продуктов в корзине"""
        total = sum(product.price * quantity for product, quantity in self.items)
        return total


# Экземпляры
milk = Perishable("Молоко", 100, 10, datetime.datetime(2023, 9, 12), 3)
vitamin_c = Vitamin("Витамин C", 200, 5, True)
apple = Product("Яблоко", 50, 20)


# Использование
cart = Cart()
cart.add_item(milk, 2)
cart.add_item(vitamin_c, 1)
cart.add_item(apple, 5)
print(cart.calculate_total())  # Вывод суммы
