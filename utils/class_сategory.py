class Category:
    title: str
    description: str
    products: list
    the_total_number_of_categories = 0
    uniq_products = 0

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.products = products
        Category.the_total_number_of_categories += 1
        Category.uniq_products += len(self.products)




