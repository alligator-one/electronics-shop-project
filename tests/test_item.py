"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

test = Item("Смартфон", 10000, 20)

def test_calculate_total_price():
    """Проверяет правильность выполнения метода, который подсчитывает total price"""
    assert test.calculate_total_price() == 200000
    assert test.quantity == 20

def test_apply_discount():
    """Проверяет правильность выполнения метода, который подсчитвает установленную скидку для конкретного товара"""
    test.pay_rate = 0.8
    test.apply_discount()
    assert test.price == 8000.0