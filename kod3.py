class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printnme(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of",
              self.graduationyear)


s1 = Student("Jan", "Kowalski", 2020)
s1.printnme()
s1.welcome()
s1.graduationyear = 2021
s1.welcome()
