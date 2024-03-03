class Category:
    title: str
    description: str
    products: list
    the_total_number_of_categories = 0
    uniq_products = 0

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.__products = products
        Category.the_total_number_of_categories += 1
        Category.uniq_products += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)

    @property
    def display_products(self):
        for product in self.__products:
            print(f'{product["name"]}, {product["price"]} руб. Остаток: {product["quantity"]}  шт.')


sss = Category("Смартфоны", "Смартфоны, как средство", [
    {"name": "Samsung Galaxy C23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
     "quantity": 5},
    {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
    {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
]
               )

sss.add_product({"name": "Xiaomi Redmi Note 12", "description": "1024GB, красный", "price": 43000.0, "quantity": 12})

sss.display_products
