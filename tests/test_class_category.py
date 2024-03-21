import pytest
from class_dir.class_product import Product
from class_dir.class_сategory import Category


@pytest.fixture
def new_category():
    category_1 = Category('Телефоны', 'мобильные телефоны')
    return category_1


@pytest.fixture
def new_good():
    product_1 = Product('Samsung', 'smth', 90_000, 2)
    return product_1


def test_goods(new_category):
    assert new_category.goods == []


def test_append_goods(new_category, new_good):
    """Тест на добавление продукта в экземпляр"""
    new_category.append_goods(new_good)
    assert new_category.name == 'Телефоны'
    assert new_category.description == 'мобильные телефоны'
    assert new_category.goods == [['Samsung', 'smth', 90_000, 2]]

    product_2 = Product('iPhone', 'smth', 100_000, 3)
    new_category.append_goods(product_2)
    assert new_category.goods == [['Samsung', 'smth', 90_000, 2], ['iPhone', 'smth', 100_000, 3]]

    product_3 = Product('iPhone', 'smth', 100_000, 8)
    new_category.append_goods(product_3)
    assert new_category.goods == [['Samsung', 'smth', 90_000, 2], ['iPhone', 'smth', 100_000, 11]]


def test_invalid_append_goods(new_category):
    """Тест на ошибку добавления объекта не являющийся Product или его наследником"""

    class Something:
        pass

    something = Something()
    assert new_category.append_goods(something) == ("Нельзя добавить объект отличный"
                                                    " от класса Product или его наследников.")


def test_counting_goods(new_category, new_good):
    """Тест на подсчет общего количества товаров"""
    assert new_category.counting_goods == 0
    new_category.append_goods(new_good)
    assert new_category.counting_goods == 2
    product_2 = Product('iPhone', 'smth', 100_000, 3)
    new_category.append_goods(product_2)
    assert new_category.counting_goods == 5


def test_get_format(new_category, new_good):
    """Тест на получение перечня товаров определенным форматом"""
    new_category.append_goods(new_good)
    assert new_category.get_format == 'Samsung, 90000 руб. Остаток: 2 шт.\n'


def test_len(new_category, new_good):
    """Тест на количество продуктов в категории"""
    new_category.append_goods(new_good)
    assert len(new_category) == 1
    product_2 = Product('iPhone', 'smth', 100_000, 3)
    new_category.append_goods(product_2)
    assert len(new_category) == 2


def test_str(new_category, new_good):
    """Тест на Отображение строкового представления"""
    new_category.append_goods(new_good)
    assert str(new_category) == "Название категории: Телефоны, количество продуктов: 1 шт."


def test_repr(new_category, new_good):
    """Тест на отображения экземпляра категории"""
    new_category.append_goods(new_good)
    assert repr(new_category) == "Телефоны, мобильные телефоны, [['Samsung', 'smth', 90000, 2]]"
    product_2 = Product('iPhone', 'smth', 100_000, 3)
    new_category.append_goods(product_2)
    assert repr(
        new_category) == "Телефоны, мобильные телефоны, [['Samsung', 'smth', 90000, 2], ['iPhone', 'smth', 100000, 3]]"


def test_average_price(new_category, new_good):
    """Тест на среднюю стоимость товаров"""
    assert new_category.average_price() == 0
    new_category.append_goods(new_good)
    product_2 = Product('iPhone', 'smth', 100_000, 9)
    new_category.append_goods(product_2)
    assert new_category.average_price() == 98181
