import csv
import os
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        price = self.price * self.quantity
        return price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Если длина наименования товара превышает 10 символов,
        то вырезает последующие после 10(и) символы.
        """
        if len(new_name) > 10:
            print('Длина наименования товара превышает 10 символов.')
        self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, data='src/items.csv'):
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        path = os.path.join(os.path.dirname(__file__), data)
        with open(path, 'r', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            for read in reader:
                cls(read['name'], read['price'], read['quantity'])

    @staticmethod
    def string_to_number(num_string):
        """
        Преобраует строку в число
        """
        return int(float(num_string))

    """Магические методы  repr и str"""
    def __repr__(self) -> str:
        return f'Item{self.__name, self.price, self.quantity}'

    def __str__(self) -> str:
        return self.__name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Cannot add Phone with non-Phone instances")