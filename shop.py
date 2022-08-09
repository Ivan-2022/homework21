from store import Store


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, title: str, quantity: int):
        if self.get_unique_items_count() >= 5:
            print("В магазине может хранится не больше 5 разных товаров")
            return "В магазине может хранится не больше 5 разных товаров"
        else:
            super().add(title, quantity)
