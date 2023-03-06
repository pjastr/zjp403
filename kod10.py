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
        return f'{self.__class__.__name__}: {self.__name}, {self.__price},' \
               f' {self.__quality}, {self.__tax}.'

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

    @staticmethod
    def check_quality(value):
        if isinstance(value, Product):
            if value.__quality > 5:
                value.__price *= 1.1


p1 = Product("Jabłko", 5.43, 6, 0)
print(p1)
Product.check_quality(p1)
print(p1)
