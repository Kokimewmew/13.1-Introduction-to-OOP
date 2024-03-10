import pytest
from class_dir.class_product import Product
from class_dir.class_сategory import Category


@pytest.fixture()
def category_phones():
    '''тестируем класс Category'''
    ct1 = Category('Phones', 'mobile phones')
    ct2 = Category('Utensil', 'Kitchen utensil')
    return ct1, ct2

def test_init(category_phones):
    '''Тестируем метод init'''
    ct1, ct2 = category_phones
    assert ct1.name == 'Phones'
    assert ct1.description == 'mobile phones'
    assert ct1.goods == []
    assert ct2.name == 'Utensil'
    assert ct2.description == 'Kitchen utensil'
    assert ct2.goods == []
    assert ct2.count_category == 2


@pytest.fixture()
def product_iphone():
    '''тест класса Product'''
    pr1 = Product('iPhone', 'the most expensive phone', 110_000, 3)
    pr2 = Product('Nokia', 'the oldest phone', 1_000, 1)
    return pr1, pr2

def test_init_pr(product_iphone):
    '''инициализируем обект класса через тест'''
    pr1, pr2 = product_iphone
    assert pr1.name == 'iPhone'
    assert pr1.description == 'the most expensive phone'
    assert pr1.price == 110_000
    assert pr1.quantity == 3
    assert pr2.name == 'Nokia'
    assert pr2.description == 'the oldest phone'
    assert pr2.price == 1_000
    assert pr2.quantity == 1
