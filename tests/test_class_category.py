import pytest

from class_dir.class_product import Product
from class_dir.class_сategory import Category


@pytest.fixture
def sport_category():
    return Category('Спорт', 'Фитнес и Тренажеры', ["Гантели", "эспандеры", "велотренажеры"])


@pytest.fixture
def spirt_category():
    return Category('Алкоголь', 'Крепкие напитки', ['Виски', 'Коньяк', 'Водка'])


def test_init_category(sport_category):
    assert sport_category.title == 'Спорт'
    assert sport_category.description == 'Фитнес и Тренажеры'
    assert sport_category.products == ["Гантели", "эспандеры", "велотренажеры"]
    assert sport_category.the_total_number_of_categories == 1
    assert sport_category.uniq_products == 3


def test_init_category_(spirt_category):
    assert spirt_category.the_total_number_of_categories == 2
    assert spirt_category.uniq_products == 6


def test_add_product(sport_category):
    new_smart = Product("OnePlus 9 Pro", "256GB, Nebula Blue", 75000.0, 0)
    sport_category.add_product(new_smart)
