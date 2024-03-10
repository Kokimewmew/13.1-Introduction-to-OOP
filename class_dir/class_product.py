class Product:
    title: str
    description: str
    price: float
    quantity: int
    count_product = 0  # Счетчик общего количества продуктов

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.count_product += 1

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

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.__price}, {self.quantity}'

    def __str__(self):
        '''Добавлено строковое отображение'''
        return f'Название продукта: {self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        ''' Метод сложения объектов (сложением сумм, умноженных на количество на складе).'''
        return (self.price * self.quantity) + (other.price * other.quantity)


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

    print(f'Метод add для 2х экземпляров класса Product: {product_1 + product_2}')

