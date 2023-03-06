class Student:
    name = 'unknown'  # class attribute

    def __init__(self):
        self.age = 20  # instance attribute

    @classmethod
    def tostring(cls):
        print('Student Class Attributes: name=', cls.name)


Student.tostring()
s1 = Student()
s1.tostring()
s1.name = "Tom"
s1.tostring()
