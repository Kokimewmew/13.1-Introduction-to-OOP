from class_dir.class_product import Product


class Category:
    name: str
    description: str
    goods: list
    count_category = 0  # Счетчик общего количества категорий
    unique_product = 0  # Общее количество уникальных продуктов

    def __init__(self, name, description):
        '''Инициализация по заданию. Атрибуты экземпляра: название, описание.
        Товары передаются списком через метод добавления.'''
        self.name = name
        self.description = description
        self.__goods = []  # Список товаров сделали приватным
        Category.count_category += 1  # при создании экземлпяра, счетчик увеличивается на 1

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
            for item in self.__goods:
                if item[0] == good.name:  # Проверяем наименование товара есть ли в списке продуктов
                    item[3] += good.quantity  # Обновляем количество товаров в продукте который уже есть
                    break
            else:
                self.__goods.append([good.name, good.description, good.price, good.quantity])  # Добавляем новый продукт
                Category.unique_product += 1
        else:
            print("Нельзя добавить объект отличный от класса Product или его наследников.")

    @property
    def counting_goods(self):
        count = 0
        for i in self.__goods:
            count += i[3]

        return count

    def __repr__(self):
        '''Метод отображения экземпляра категории'''
        return f'{self.name}, {self.description}, {self.__goods}'

    @property
    def get_format(self):
        '''добавлен геттер для вывода необходимого формата'''
        result = ''
        for good in self.__goods:
            result += f'{good[0]}, {good[2]} руб. Остаток: {good[3]} шт.\n'
        return result

    def __len__(self):
        '''Вывод количества продуктов на складе'''
        return len(self.__goods)

    def __str__(self):
        '''Добавлено строковое отображение'''
        return f'Название категории: {self.name}, количество продуктов: {self.__len__()} шт.'


if __name__ == '__main__':
    category_1 = Category('Телефоны', 'мобильные телефоны')  # Экземпляр класса Category
    product_1 = Product('Samsung', 'smth', 90_000, 2)  # Экземпляр класса Product
    product_2 = Product('iPhone', 'smth', 100_000, 3)  # Экземпляр класса Product
    print(category_1.goods)

    category_1.append_goods(product_1)  # Добавление продукта в приватный список товаров
    print(category_1.goods)
    category_1.append_goods(product_2)  # Добавление продукта в приватный список товаров
    print(category_1.goods)

    product_3 = Product('iPhone', 'smth', 100_000, 34)
    category_1.append_goods(product_3)  # Добавление продукта в приватный список товаров если такой продукт существует
    print(category_1.goods)  # Отображение приватного списка товаров

    print(f'Уникальных продуктов: {category_1.unique_product}')  # Количество уникальных товаров в приватном списке
    print(category_1.get_format)  # Получение перечня товаров определенным форматом
    print(str(category_1))  # Отображение строкового представления

    print(f'Вывод  общего количества продуктов категории: {category_1.counting_goods}')

    class Something:
        pass

    something = Something()
    category_1.append_goods(something)


