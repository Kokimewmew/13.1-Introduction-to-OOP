from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def launch_product(cls, new_product):
        '''Класс-метод по добавлению новых товаров'''


class MixinLog:
    """Класс миксин для вывода __repr__"""

    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        """вывод __repr__"""
        list_attr = []
        for i in self.__dict__.items():
            list_attr.append(i[1])

        return f'Создание нового экземпляра продукта - {self.__class__.__name__}{tuple(list_attr)}'


class Product(MixinLog, AbstractProduct):
    title: str
    description: str
    price: float
    quantity: int
    count_product = 0  # Счетчик общего количества продуктов

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity <= 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        self.quantity = quantity
        Product.count_product += 1
        super().__init__()

    @classmethod
    def launch_product(cls, new_product):
        '''Класс-метод по добавлению новых товаров'''
        return cls(**new_product)

    @property
    def price(self):
        '''геттер - установка цены'''
        return self.__price

    @price.setter
    def price(self, value):
        '''сеттер - условие, если цена <= 0, то вывод сообщения, иначе вывод заданной цены'''
        if value <= 0:
            print("цена введена некорректная")
        else:
            if self.__price > value:
                input_user = input("Подтвердите понижение стоимости (y/n):\n").strip()
                if input_user == "y":
                    self.__price = value
                else:
                    print("Цена не изменилась")
            else:
                self.__price = value

    def __str__(self):
        '''Добавлено строковое отображение'''
        return f'Название продукта: {self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        ''' Метод сложения объектов (сложением сумм, умноженных на количество на складе).'''
        if self.__class__.__name__ == other.__class__.__name__:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, productivity, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.productivity = productivity
        self.model = model
        self.memory = memory
        self.color = color


class Lawngrass(Product):

    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color


if __name__ == '__main__':
    # Создание словаря для дальнейшего добавления в экземпляры класса
    new_product_3 = {
        'name': 'Nokia',
        'description': 'smth',
        'price': 1000,
        'quantity': 10
    }

    product_3 = Product.launch_product(new_product_3)  # Добавление нового продукта
    print(product_3)  # Вывод добавленного словаря

    product_1 = Product('Samsung', 'smth', 90_000, 2)
    print(product_1)
    product_2 = Product('iPhone', 'smth', 100_000, 3)  # Экземпляр класса Product

    lawngrass_1 = Lawngrass("трава", "газонная", 100, 3, "Russia", "5 лет", "зеленая")

    print(f'Метод add для 2х экземпляров класса Product: {product_1 + product_2}')

    # print(f'Метод add для 2х экземпляров класса Product: {product_1 + lawngrass_1}')
