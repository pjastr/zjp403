class Product:

    def __init__(self, name, price, quality, tax):
        if not isinstance(name, str):
            name = ''
        self.__name = name
        if price < 0:
            price = 0
        self.__price = price
        if quality < 0:
            quality = 0
        self.__quality = quality
        if tax < 0:
            tax = 0
        self.__tax = tax

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__name}, {self.__price}, ' \
               f'{self.__quality}, {self.__tax}.'

    @property
    def tax(self):
        return self.__tax

    @tax.setter
    def tax(self, value):
        if value < 0:
            value = 0
        self.__tax = value

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quality(self):
        return self.__quality


class Book(Product):

    def __init__(self, name, price, quality, tax, authors, title):
        super().__init__(name, price, quality, tax)
        if len(authors) > 0:
            authors = ['Adam Mickiewicz']
        self.__authors = authors
        self.__title = title
        self.tax = 0

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}, {self.price},' \
               f' {self.quality}, {self.tax}' \
               f', {self.__authors}, {self.__title}.'


p1 = Product("Mleko", 8.23, 2, 0.23)
print(p1)
b1 = Book("Książka", 30.23, 5, 0.05, ['Adam Mickiewicz'], 'Pan Tadeusz')
print(b1)
