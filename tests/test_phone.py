from src.phone import Phone


def test___init__():
    phone = Phone("iPhone 16", 150000, 4, 2)
    assert phone.name == "iPhone 16"
    assert phone.price == 150000
    assert phone.quantity == 4
    assert phone.number_of_sim == 2


def test_repr():
    phone1 = Phone("iPhone 16", 150000, 4, 2)
    assert repr(phone1) == "Phone('iPhone 16', 150000, 4, 2)"


def test_str():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone1) == 'iPhone 14'