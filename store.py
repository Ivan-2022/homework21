from storage import Storage


class Store(Storage):
    def __init__(self, items, capacity=100):
        self.items = items
        self.capacity = capacity

    def __repr__(self):
        st = ""
        for key, value in self.items.items():
            st += f"{key}: {value}\n"
        return st

    def add(self, title: str, quantity: int):
        if title in self.items.keys():
            if self.get_free_space() >= quantity:
                self.items[title] += quantity
            else:
                space = quantity - self.get_free_space()
                self.items[title] += self.get_free_space()
                print(f"Товар добавлен не весь, т.к. превышена вместимость на {space}")
                return f"Товар добавлен не весь, т.к. превышена вместимость на {space}"
        else:
            if self.get_free_space() >= quantity:
                self.items[title] = quantity
            else:
                space = quantity - self.get_free_space()
                self.items[title] = self.get_free_space()
                print(f"Товар добавлен не весь, т.к. превышена вместимость на {space}")
                return f"Товар добавлен не весь, т.к. превышена вместимость на {space}"

    def remove(self, title: str, quantity: int):
        if quantity < self.items[title]:
            self.items[title] -= quantity
        else:
            space = quantity - self.items[title]
            self.items[title] = 0
            print(f"Не хватило на складе {space} шт")
            return f"Не хватило на складе {space} шт"

    def get_free_space(self):
        counter = 0
        for value in self.items.values():
            counter += value
        free_space = self.capacity - counter
        return free_space

    @property
    def get_items(self):
        return self.items

    @get_items.setter
    def get_items(self, items: dict):
        self.items = items

    def get_unique_items_count(self):
        return len(self.items.keys())


# store = Store(items={"Печеньки": 3, "Собачки": 25, "Коробки": 40}, capacity=100)

# store.add("Печеньки", 90)
# store.remove("Собачки", 21)
# print(store.get_free_space())
# print(store.items)
# print(store.get_unique_items_count())
