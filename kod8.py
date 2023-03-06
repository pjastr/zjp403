from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def frombirthyear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isadult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.frombirthyear('mayank', 1996)

print(person1.age)
print(person2.age)

print(Person.isadult(22))
