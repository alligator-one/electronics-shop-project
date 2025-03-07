from src.item import Item
from src.phone import Phone

data = Item("Смартфон", 10000, 20)


class Tests:
    def test_calculate_total_price(self):
        """Проверяет правильность выполнения метода, который подсчитывает total price"""
        assert data.calculate_total_price() == 200000
        assert data.quantity == 20

    def test_apply_discount(self):
        """Проверяет правильность выполнения метода, который подсчитвает установленную скидку для конкретного товара"""
        data.pay_rate = 0.8
        data.apply_discount()
        assert data.price == 8000.0

    def test_name(self):
        """Тест сеттера name"""
        # data.name = "Смартфон"
        assert data.name == 'Смартфон'

    def test_name(self):
        """Тест сеттера сокращающего длину имени до 10(и) символов."""
        data.name = "Abrakadabra"
        assert len(data.name) == 10
    def test_instantiate_from_csv(self):
        """
        Проверка метода инициализируеющнго экземпляры класса Item данными из файла src/items.csv
        """
        Item.instantiate_from_csv('items.csv')
        assert len(Item.all) == 5

    def test_string_to_number(self):
        """
        Проверка метода преоброзвания строки в число
        """
        assert data.string_to_number('200') == 200
        assert data.string_to_number('200.0') == 200
        assert data.string_to_number('200.5') == 200
        assert data.string_to_number('200.55') == 200
        assert data.string_to_number('200.') == 200

def test__repr__():
    """
    Тест магического метода repr
    """
    data.name = 'Смартфон'
    assert repr(data) == "Item('Смартфон', 8000.0, 20)"

def test_add():
    item2 = Item('Телефон', 10000, 5)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item2 + phone1 == 10


def test__str__():
    data.name = "Смартфон"
    """
    Тест магического метода str
    """

    assert str(data) == 'Смартфон'