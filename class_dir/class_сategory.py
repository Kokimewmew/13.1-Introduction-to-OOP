from class_dir.class_product import product_1, product_2, product_3, Product


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

    @property
    def products(self) -> str:
        result = ''
        for product in self.__products:
            result += f'{product.title}, {product.price} руб. Остаток: {product.quantity} шт.\n'

        return result

    def add_product(self, s):
        self.__products.append(s)


category_smart = Category("Смартфоны", "Смартфоны, как средство", [product_1, product_2, product_3])
print(category_smart.products)

new_smart = Product("OnePlus 9 Pro","256GB, Nebula Blue", 75000.0, 0)
category_smart.add_product(new_smart)

print(category_smart.products)
