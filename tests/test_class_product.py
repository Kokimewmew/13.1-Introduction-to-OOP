import pytest
from utils.class_product import Product


@pytest.fixture
def sport_product():
    return Product('Гантели', '20 кг', 1550.0, 10)


def test_init_product(sport_product):
    assert sport_product.title == 'Гантели'
    assert sport_product.description == '20 кг'
    assert sport_product.price == 1550.0
    assert sport_product.quantity == 10
