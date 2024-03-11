import pytest
from class_dir.class_product import Product


@pytest.fixture
def new_product():
    return {
        "name": "Coffee",
        "description": "Delicious coffee beans",
        "price": 10.0,
        "quantity": 100
    }


def test_product_creation(new_product):
    product = Product(**new_product)
    assert product.name == "Coffee"
    assert product.description == "Delicious coffee beans"
    assert product.price == 10.0
    assert product.quantity == 100


def test_price_setter(new_product):
    product = Product(**new_product)
    product.price = 12.0
    assert product.price == 12.0


def test_negative_price_setter(new_product, capsys):
    product = Product(**new_product)
    product.price = -5.0
    captured = capsys.readouterr()
    assert "цена введена некорректная" in captured.out


def test_price_lower_confirm(new_product, capsys, monkeypatch):
    product = Product(**new_product)
    monkeypatch.setattr('builtins.input', lambda _: "y")
    product.price = 8.0
    assert product.price == 8.0


def test_price_lower_cancel(new_product, capsys, monkeypatch):
    product = Product(**new_product)
    monkeypatch.setattr('builtins.input', lambda _: "n")
    product.price = 8.0
    assert product.price == 10.0


def test_addition(new_product):
    product1 = Product(**new_product)
    product2 = Product(name="Tea", description="Refreshing tea leaves", price=5.0, quantity=50)
    total_value = product1 + product2
    assert total_value == 1250.0  # (10.0 * 100) + (5.0 * 50) = 1000 + 500 = 1250
