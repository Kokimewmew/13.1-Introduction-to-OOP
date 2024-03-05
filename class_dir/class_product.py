class Product:
    title: str
    description: str
    price: float
    quantity: int

    def __init__(self, title, description, price, quantity):
        self.__title = title
        self.__description = description
        self.__price = price
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price
    @property
    def title(self):
        return self.__title

    @property
    def quantity(self):
        return self.__quantity

    @price.setter
    def price(self, value):
        if 0 >= value:
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

    @classmethod
    def add_products(cls, new_product):
        title, description, price, quantity = new_product

        return cls(title, description, price, quantity)


product_1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


print(product_1.price)


new_product = ["Iphone 15", "512GB, Gray space", 210000.0, 8]

product_4 = Product.add_products(new_product)

print(product_2.price)

product_2.price = float(5)

print(product_2.price)

