from store import Store
from shop import Shop


class Request:
    def __init__(self, request: str):
        self.request = request
        action = request.split()
        self.__amount = int(action[1])
        self.__product = action[2]
        self.__from = action[4]
        self.__to = action[6]

        if self.__to == 'магазин':
            self.__to = 'shop'
        if self.__to == 'склад':
            self.__to = 'store'
        if self.__from == 'магазин':
            self.__from = 'shop'
        if self.__from == 'склад':
            self.__from = 'store'
        if self.__from == 'ниоткуда':
            self.__from = None
        if self.__to == 'никуда':
            self.__to = None

    def move(self):
        if self.__from and self.__to:
            eval(self.__from).remove(self.__product, self.__amount)
            eval(self.__to).add(self.__product, self.__amount)
        elif self.__to:
            eval(self.__to).add(self.__product, self.__amount)
        elif self.__from:
            eval(self.__from).remove(self.__product, self.__amount)


store = Store(items={"печеньки": 10, "собачки": 10, "коробки": 20, "конфеты": 10, "котята": 15, "ящики": 20})
shop = Shop(items={"печеньки": 3, "собачки": 5, "коробки": 6})
