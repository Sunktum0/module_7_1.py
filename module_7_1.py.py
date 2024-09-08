import uuid

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'  # Инкапсулированный атрибут имени файла

    def get_products(self):
        """Считывает всю информацию из файла и возвращает ее как строку."""
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return 'No products found.'

    def add(self, *products):
        """Добавляет продукты в файл, если их нет по названию."""
        existing_products = set()

        # Считываем существующие продукты, чтобы избежать дублирования
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    existing_products.add(line.strip().split(', ')[0])  # Добавляем только название продукта
        except FileNotFoundError:
            print("Файл не найден, создается новый.")

        for product in products:
            if product.name in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')
                print(f'Добавлен продукт: {product.name}')


# Пример работы программы:
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')  # Обратите внимание на то, что это другой объект, но с тем же названием

    print(p2)  # Печатаем строковое представление продукта

    s1.add(p1, p2, p3)  # Добавляем продукты в магазин
    print(s1.get_products())  # Выводим все продукты из файла