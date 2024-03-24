from class_dir.class_product import Product
from abc import ABC, abstractmethod


class AbstractCategory(ABC):
    @abstractmethod
    def __init__(self):
        '''Абстрактный метод инициализации'''


class Category(AbstractCategory):
    name: str
    description: str
    goods: list
    count_category = 0  # Счетчик общего количества категорий
    unique_product = 0  # Общее количество уникальных продуктов

    def __init__(self, name, description, goods):
        '''Инициализация по заданию. Атрибуты экземпляра: название, описание.
        Товары передаются списком через метод добавления.'''
        self.name = name
        self.description = description
        self.__goods = goods  # Список товаров сделали приватным
        Category.unique_product += len(self.__goods)  # Счетчик увеличивается на уникальное кол-во товаров в категории
        Category.count_category += 1  # при создании экземпляра, счетчик увеличивается на 1

    @property
    def goods(self):
        '''Данный метод позволяет принтом вывести приватный список товаров'''
        return self.__goods

    def append_goods(self, good):
        '''
         Метод добавления товаров в список
        также данный метод считает итоговое количество всех продуктов в сумме
        '''
        if isinstance(good, Product):
            if good.quantity <= 0:
                raise ValueError('Товар с нулевым количеством не может быть добавлен')
            for item in self.__goods:
                if item.name == good.name:  # Проверяем наименование товара есть ли в списке продуктов
                    item.quantity += good.quantity  # Обновляем количество товаров в продукте который уже есть
                    break
            else:
                self.__goods.append([good.name, good.description, good.price, good.quantity])  # Добавляем новый продукт
        else:
            return f"Нельзя добавить объект отличный от класса Product или его наследников."


    def __repr__(self):
        '''Метод отображения экземпляра категории'''
        return f'{self.name}, {self.description}, {self.__goods}'

    @property
    def get_format(self):
        '''добавлен геттер для вывода необходимого формата'''
        result = ''
        for good in self.__goods:
            result += f'{good.name}, {good.price} руб. Остаток: {good.quantity} шт.\n'
        return result

    def average_price(self):
        """Метод на нахождение средней стоимости товаров"""
        result = 0
        for good in self.__goods:
            result += good.price * good.quantity
        try:
            result = int(result / self.__len__())
        except ZeroDivisionError:
            print("Деление на 0 количество товаров")
        return result

    def __len__(self):
        '''Вывод количества продуктов на складе'''
        count = 0
        for good in self.__goods:
            count += good.quantity

        return count

    def __str__(self):
        '''Добавлено строковое отображение'''
        return f'Название категории: {self.name}, количество продуктов: {len(self.__goods)} шт.'


if __name__ == '__main__':
    product_1 = Product('Samsung', 'smth', 90_000, 2)  # Экземпляр класса Product
    product_2 = Product('iPhone', 'smth', 100_000, 3)  # Экземпляр класса Product
    category_1 = Category('Телефоны', 'мобильные телефоны', [product_1, product_2])  # Экземпляр класса Category

    product_3 = Product('iPhone', 'smth', 100_000, 34)
    category_1.append_goods(product_3)  # Добавление продукта в приватный список товаров если такой продукт существует
    print(category_1.get_format)  # Получение перечня товаров определенным форматом
    print(str(category_1))  # Отображение строкового представления

    print(f'Вывод  общего количества продуктов категории на складе: {category_1.__len__()}')
    print(category_1.average_price())
