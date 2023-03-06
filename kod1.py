class Person(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee(Person):

    def is_employee(self):
        return True


emp = Person("Bartek")
print(emp.get_name(), emp.is_employee())

emp = Employee("Sylwia")
print(emp.get_name(), emp.is_employee())
